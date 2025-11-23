import streamlit as st
import pandas as pd

st.set_page_config(page_title="Counseling", page_icon="🐆", layout="wide",
                   initial_sidebar_state="collapsed")

st.write(f"Your current traits are {st.session_state.goal1}, {st.session_state.goal2},"
         f" {st.session_state.mood1}, and {st.session_state.mood2}")

st.image("RoaryWelcomeWIP.png", width=500)
st.write(f"\"WOOHOO {st.session_state.name}, here's a schedule that I think will work "
         f"much better for you!\"")

classdf = pd.read_csv("PoeticClasses.csv")

user_selections_mapped = [
    ('Goal', st.session_state.goal1 if 'goal1' in st.session_state else 'Learn'),
    ('Goal', st.session_state.goal2 if 'goal2' in st.session_state else 'Challenge'),
    ('Mood', st.session_state.mood1 if 'mood1' in st.session_state else 'Curious'),
    ('Mood', st.session_state.mood2 if 'mood2' in st.session_state else 'Joyous')]

final_selections_list = []
failed_selections = []
already_picked_course_names = set()

for column_name, selected_value in user_selections_mapped:

    # Filter the DataFrame for the specific column and value
    filtered_df = classdf[classdf[column_name] == selected_value]

    # Filter OUT any courses we have already selected in a previous loop iteration
    available_courses_df = filtered_df[
        ~filtered_df['Class Name'].isin(already_picked_course_names)
    ]

    if not available_courses_df.empty:
        # Sample 1 random course from what's available
        sampled_row = available_courses_df.sample(n=1, replace=False)

        # Add the selected CourseName to our set of picked names
        picked_name = sampled_row['Class Name'].iloc
        already_picked_course_names.add(picked_name)

        # Append the sampled DataFrame row to our results list
        final_selections_list.append(sampled_row)
    else:
        failed_selections.append(f"{column_name}: {selected_value}")

# Combine the list of single-row DataFrames into one final DataFrame
if final_selections_list:
    final_result_df = pd.concat(final_selections_list)
else:
    final_result_df = pd.DataFrame(columns=classdf.columns)

st.dataframe(data=final_result_df, row_height=150)

# Display ENTIRE excel file I started with
with st.expander("Full Course Catalog"):
    st.dataframe(classdf)


