import json
import tempfile
import zipfile
from io import StringIO
from typing import Dict

import pandas
from flask import Flask, request, render_template
import os

from investments.ibdds import ibdds
from investments.ibtax import ibtax


UPLOAD_FOLDER = 'C:/Nina/github/investments/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def download_and_extract(zip_file, dir_name: str) -> (str, tempfile.TemporaryDirectory):
    type(zip_file)
    tmpdirname = tempfile.TemporaryDirectory(dir=UPLOAD_FOLDER)
    path_to_zip_file = os.path.join(tmpdirname.name, zip_file.filename)
    zip_file.save(path_to_zip_file)
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        directory_to_extract_to = os.path.join(tmpdirname.name, dir_name)
        zip_ref.extractall(directory_to_extract_to)
        return directory_to_extract_to, tmpdirname

def download(csc_file, dir_path: str) -> (str, tempfile.TemporaryFile):
    tmpfile = tempfile.TemporaryFile(dir=dir_path)
    print(type(tmpfile))
    path_to_csv_file = os.path.join(dir_path, csc_file.filename)
    csc_file.save(path_to_csv_file)
    return path_to_csv_file, tmpfile

def my_default(obj):
    from investments.ticker import TickerKind
    if isinstance(obj, TickerKind):
        return str(obj)


def to_json(res: Dict[str, str]) -> str:
    r = ""
    for key in res:
        value = res[key]
        if isinstance(value, pandas.DataFrame):
            r += f'"{key}" : {value.to_json(orient="records")}, '
    return "{" + r[:-2] + "}"


@app.route("/ibtax/", methods=["GET", "POST"])
def tax():

    if request.method == "POST":
        activity_path, activity_dir = download_and_extract(request.files['file1'], "activity")
        confirmation_path, confirmation_dir = download_and_extract(request.files['file2'], "confirmation")

        res = ibtax.run(activity_path, confirmation_path)

        activity_dir.cleanup()
        confirmation_dir.cleanup()

        r = to_json(res)
        print(r)
        return r
    else:
        return render_template("upload.html")

@app.route("/ibdds/", methods=["GET", "POST"])
def activity():

    if request.method == "POST":
        file1 = request.files['file1']
        activity_path = os.path.join(app.config['UPLOAD_FOLDER'], "activity")
        activity_file_path, tmp_file = download(file1, activity_path)
        res = ibdds.run(activity_file_path)
        tmp_file.close()
        return json.dumps(res, default=my_default)
    else:
        return render_template("activity_report.html")