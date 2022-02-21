import json
from pathlib import Path

import pytest


@pytest.mark.parametrize("test_app", [{"buildername": "needs", "srcdir": "doc_test/doc_needs_builder"}], indirect=True)
def test_doc_needs_builder(test_app):
    app = test_app
    app.build()

    needs_json = Path(app.outdir, "needs.json")
    with open(needs_json) as needs_file:
        needs_file_content = needs_file.read()

    needs_list = json.loads(needs_file_content)
    assert needs_list["versions"]["1.0"]
    assert needs_list["versions"]["1.0"]["needs"]["TC_NEG_001"]

    # needs builder added new version needs from needs_files
    assert needs_list["versions"]["2.0"]
    assert needs_list["versions"]["2.0"]["needs"]["TEST_01"]


@pytest.mark.parametrize(
    "test_app", [{"buildername": "needs", "srcdir": "doc_test/doc_needs_builder_negative_tests"}], indirect=True
)
def test_doc_needs_build_without_needs_file(test_app):
    import os
    import subprocess

    app = test_app

    srcdir = Path(app.srcdir)
    out_dir = os.path.join(srcdir, "_build")

    out = subprocess.run(["sphinx-build", "-b", "needs", srcdir, out_dir], capture_output=True)
    assert not out.stderr
    assert "needs.json found, but will not be used because needs_file not configured." in out.stdout.decode("utf-8")


@pytest.mark.parametrize("test_app", [{"buildername": "needs", "srcdir": "../docs"}], indirect=True)
def test_needs_official_doc(test_app):
    app = test_app
    app.build()


@pytest.mark.parametrize(
    "test_app", [{"buildername": "html", "srcdir": "doc_test/doc_needs_builder_parallel"}], indirect=True
)
def test_needs_html_and_json(test_app):
    """
    Build html output and needs.json in one sphinx-build
    """
    import json
    import os
    import subprocess

    app = test_app
    app.build()

    needs_json_path = os.path.join(app.outdir, "needs.json")
    assert os.path.exists(needs_json_path)

    srcdir = app.srcdir
    build_dir = os.path.join(app.outdir, "../needs")
    subprocess.run(["sphinx-build", "-b", "needs", srcdir, build_dir], capture_output=True)
    needs_json_path_2 = os.path.join(build_dir, "needs.json")
    assert os.path.exists(needs_json_path_2)

    # Check if the needs.json files from html/parallel build and builder are the same
    with open(needs_json_path) as f1:
        needs_1 = json.load(f1)
        with open(needs_json_path_2) as f2:
            needs_2 = json.load(f2)

            # Just check need-data, as the rest contains not matching timestamps
            need_data_1 = needs_1["versions"]["1.0"]["needs"]
            need_data_2 = needs_2["versions"]["1.0"]["needs"]
            assert need_data_1 == need_data_2