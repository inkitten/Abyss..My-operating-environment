from plugins.internals.knowledge.main import get_note_path, remove_note


def test_rejects_path_traversal(tmp_path):
    assert get_note_path(tmp_path, "../evil") is None


def test_accepts_normal_name(tmp_path):
    assert get_note_path(tmp_path, "meeting") == tmp_path / "meeting.md"


def test_remove_cannot_delete_outside_notes_dir(tmp_path):
    notes = tmp_path / "notes"
    notes.mkdir()
    victim = tmp_path / "victim.md"
    victim.write_text("keep me")
    remove_note(notes, "../victim")
    assert victim.exists()
