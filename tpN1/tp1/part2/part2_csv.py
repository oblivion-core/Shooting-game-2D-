#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP N1 - Part 2 : read the M1 GSI canvas CSV and build nested dictionaries
import csv
import json


# ---------- Step 1 : two levels  (semester -> unit -> [modules]) ----------
def csv_to_nested_dict(csv_file):
    data = {"S1": {}, "S2": {}}
    with open(csv_file, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")   # the file is TAB separated
        for row in reader:
            semester = row["semester"]
            unite = row["unit"]
            module = {
                "module_name": row["module_name"],
                "module_title": row["module_title"],
                "coef": int(row["coef"]),
                "credit": int(row["credit"]),
                "percent_tp": float(row["percent_tp"]),
                "percent_td": float(row["percent_td"]),
                "percent_exam": float(row["percent_exam"]),
            }
            if unite not in data[semester]:
                data[semester][unite] = []          # a unit = list of modules
            data[semester][unite].append(module)
    return data


# ---------- Step 2 : three levels (semester -> unit -> module) ----------
def csv_to_nested_dict3(csv_file):
    data = {}
    with open(csv_file, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            semester, unite, module_name = row["semester"], row["unit"], row["module_name"]
            data.setdefault(semester, {})
            data[semester].setdefault(unite, {})    # a unit = dict of modules
            data[semester][unite][module_name] = {  # module_name is now a KEY
                "unit_title": row["unit_title"],
                "module_title": row["module_title"],
                "coef": int(row["coef"]),
                "credit": int(row["credit"]),
                "percent_tp": float(row["percent_tp"]),
                "percent_td": float(row["percent_td"]),
                "percent_exam": float(row["percent_exam"]),
            }
    return data


# ---------- Step 3 : JSON display ----------
def to_json(data):
    # ensure_ascii=False keeps accents (é, è...) readable
    return json.dumps(data, indent=4, ensure_ascii=False)


# ---------- Step 4 : HTML (works with the 3-level dictionary) ----------
def modules_to_html(data):
    html = ['<html><head><meta charset="utf-8">',
            '<title>M1 GSI canvas</title>',
            '<style>table{border-collapse:collapse;margin-bottom:12px}'
            'th,td{border:1px solid #444;padding:4px 8px}'
            'th{background:#ddd}</style>',
            '</head><body>']
    for semester, unites in data.items():
        html.append(f"<h2>Semester {semester}</h2>")
        for unite, modules in unites.items():
            first = next(iter(modules.values()))
            html.append(f"<h3>{unite} - {first['unit_title']}</h3>")
            html.append("<table>")
            html.append("<tr><th>Module Code</th><th>Title</th><th>Coef</th><th>Credit</th>"
                        "<th>TP%</th><th>TD%</th><th>Exam%</th></tr>")
            for code, info in modules.items():
                html.append("<tr>")
                html.append(f"<td>{code}</td>")
                html.append(f"<td>{info['module_title']}</td>")
                html.append(f"<td>{info['coef']}</td>")
                html.append(f"<td>{info['credit']}</td>")
                # values are already percentages (20, 40, 60): NO "* 100" here
                html.append(f"<td>{info['percent_tp']:.0f}%</td>")
                html.append(f"<td>{info['percent_td']:.0f}%</td>")
                html.append(f"<td>{info['percent_exam']:.0f}%</td>")
                html.append("</tr>")
            html.append("</table>")
            html.append("<hr>")
    html.append("</body></html>")
    return "\n".join(html)


if __name__ == "__main__":
    filename = "modules.csv"

    print("=== 2 levels (semester -> unit) ===")
    print(to_json(csv_to_nested_dict(filename)))

    print("\n=== 3 levels (semester -> unit -> module) ===")
    result = csv_to_nested_dict3(filename)
    print(to_json(result))

    with open("modules.json", "w", encoding="utf-8") as f:
        f.write(to_json(result))
    with open("modules.html", "w", encoding="utf-8") as f:
        f.write(modules_to_html(result))
    print("\nFiles generated: modules.json, modules.html")

    # bonus: quick access example
    print("MTI credit:", result["S1"]["U3_S1"]["MTI"]["credit"])
