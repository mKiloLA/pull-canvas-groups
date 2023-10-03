from canvasapi import Canvas
import pandas as pd
import tomllib
import os

def get_user_data(course_number):
    with open("config.toml", "rb") as f:
        data = tomllib.load(f)

    API_URL = data["canvas"]["url"]
    API_KEY = data["canvas"]["token"]

    student_info = pd.DataFrame(columns=["Section", "Team", "Name", "Email"])
    try:
        canvas = Canvas(API_URL, API_KEY)
        course = canvas.get_course("17260000000" + course_number)
        course_name = course.name
        groups = course.get_groups()
        for group in groups:
            group_name = group.name
            users = group.get_users()
            for user in users:
                user_profile = user.get_profile()
                user_dict = {"Section": course_name,
                             "Team": group_name,
                             "Name": user_profile["name"],
                             "Email": user_profile["primary_email"]
                }
                student_info = pd.concat([student_info, pd.DataFrame(user_dict, index=[0])], ignore_index=True)
        output_filename = os.path.expanduser("~")+"/Downloads/"+course_name+".xlsx"
        student_info = student_info.drop_duplicates()
        student_info.to_excel(output_filename, index=False, header=True)
    except Exception as e:
        print(e)
