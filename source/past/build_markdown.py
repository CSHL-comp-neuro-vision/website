import json
import pandas as pd
import numpy as np

# To generate the participants.json contents, you can use this prompt with chatGPT:

# Here is an HTML table:
# <Copy+paste table directly from current site here, don't worry that the formatting is weird>
# Organize the table to use this JSON format:
# {
#     "Year": "2004",
#     "Organizers": ["First Last"],
#     "Teaching Assistants": ["First Last"],
#     "Lecturers": ["First Last" ],
#     "Students": ["First Last"]
# }

def idx_of_name(df, name):
    return np.argmax(df["Name"].values == name)

def generate_html_from_json(json_data, website_data):
    html = ""
    for table in json_data:
        html += f"## {table['Year']}\n\n"
        html += f"**Cold Spring Harbor Laboratory, {table['Year']}**\n\n"
        html += f'<div style="display:block;text-align:left"><img border="0" src="../_static/images/past/{table["Year"]}.jpg" style="width:100%" /></div>'
        html += '<div><hr /></div>'
        html += "\n"
        html += '<table class="tg">'
        html += '<thead>'
        html += '<tr>'
        html += '<th class="tg-pgjb"><span style="font-weight:bold">Organizers</span></th>'
        for organizer in table["Organizers"]:
            last = organizer.split(' ')[1]
            if last in website_data["Name"].values:
                index = idx_of_name(website_data, last)
                link = website_data["Website"].values[index]
                html += f'<td class="tg-zv4m"><a href="{link}" target="_blank" rel="noopener noreferrer">{organizer}</a></td>'
            else:
                html += f'<td class="tg-zv4m">{organizer}</td>'
        html += '</tr>'
        html += '</thead>'
        html += "\n"
        html += '<tbody>'
        html += "\n"
        html += '<tr>'
        html += '<th class="tg-ml8a">Teaching Assistants</th>'
        for ta in table["Teaching Assistants"]:
            last = ta.split(' ')[1]
            if last in website_data["Name"].values:
                index = idx_of_name(website_data, last)
                link = website_data["Website"].values[index]
                html += f'<td class="tg-zv4m"><a href="{link}" target="_blank" rel="noopener noreferrer">{ta}</a></td>'
            else:
                html += f'<td class="tg-zv4m">{ta}</td>'
        html += '</tr>'
        html += "\n"
        html += '<tr>'
        html += '<th class="tg-ml8a">Lecturers</th>'

        # for lecturer in table["Lecturers"]:
        #     last = lecturer.split(' ')[1]
        #     if last in website_data["Name"].values:
        #         index = idx_of_name(website_data, last)
        #         link = website_data["Website"].values[index]
        #         html += f'<td class="tg-zv4m"><a href="{link}" target="_blank" rel="noopener noreferrer">{lecturer}</a></td>'
        #     else:
        #         html += f'<td class="tg-zv4m">{lecturer}</td>'
        
        lecturers = table["Lecturers"]
        num_lecturers = len(lecturers)
        for i in range(0, num_lecturers, 7):
            group_lecturers = lecturers[i:i+7]
            group_html = ""
            for lecturer in group_lecturers:
                last = lecturer.split(' ')[1]
                if last in website_data["Name"].values:
                    index = idx_of_name(website_data, last)
                    link = website_data["Website"].values[index]
                    group_html += f'<a href="{link}" target="_blank" rel="noopener noreferrer">{lecturer}</a><br>'
                else:
                    group_html += f'{lecturer}<br>'

            html += f'<td class="tg-zv4m">{group_html}</td>'

        html += '</tr>'
        html += "\n"
        html += '<tr>'
        html += '<th class="tg-ml8a">Students</th>'
        # for student in table["Students"]:
        #     html += f'<td class="tg-zv4m">{student}</td>'

        students = table["Students"]
        num_students = len(students)
        for i in range(0, num_students, 10):
            group_students = students[i:i+10]
            group_html = ""
            for student in group_students:
                group_html += f'{student}<br>'

            html += f'<td class="tg-zv4m">{group_html}</td>'

        html += '</tr>'
        html += "\n"
        html += '</tbody>'
        html += '</table>'
        html += "\n"
        html += '<br><br><br>'
        html += "\n\n"
    return html

with open("participants.json", "r") as file:
    # Load the JSON data from the file
    json_data = json.load(file)

website_data = pd.read_csv("websites_no_duplicates.csv")

html_content = generate_html_from_json(json_data, website_data)

md_content = """# Past Courses & Alumni


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-ml8a{background-color:#66ccff;border-color:#66ccff;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-pgjb{background-color:#66ccff;border-color:#66ccff;text-align:left;vertical-align:top}
</style>\n\n"""

md_content += html_content

with open("output.md", "w") as file:
    file.write(md_content)