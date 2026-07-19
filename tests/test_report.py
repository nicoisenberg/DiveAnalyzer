from src.report import save_report


def test_save_report(tmp_path):
    
    report_text = "Test report"
    output_path = tmp_path / "report.txt"

    save_report(report_text, output_path)

    assert output_path.exists()

    saved_text = output_path.read_text(encoding="utf-8")

    assert saved_text == report_text               