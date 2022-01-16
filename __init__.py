from anki.hooks import wrap
from anki.notes import Note
from aqt.browser.browser import Browser
from aqt.qt import *
from aqt.utils import showInfo
from aqt import mw
import html
import re

config = mw.addonManager.getConfig(__name__)

# https://stackoverflow.com/a/19730306
TAG_PATTERN = re.compile(r"(<!--.*?-->|<[^>]*>)")


def update_config(new_config):
    global config
    config = new_config


def strip_html(text: str) -> str:
    text = TAG_PATTERN.sub("", text)
    text = html.unescape(text)

    return text.strip()


def format_note(note: Note) -> str:
    text = note.values()[config["field_index"]]
    if config["strip_html"]:
        text = strip_html(text)
    return text


def copy_selection_field(self) -> None:
    global config
    config = mw.addonManager.getConfig(__name__)  # reload config if changed

    clipboard = QApplication.clipboard()
    selection_field = [
        format_note(self.col.get_note(card)) for card in self.selected_notes()
    ]
    clipboard.setText(config["separator"].join(selection_field))


def setupMenus(self) -> None:
    self.form.actionCopySelectionField = QAction("Copy Selection Field", self)
    self.form.actionCopySelectionField.setShortcut("Ctrl+Shift+C")
    self.form.actionCopySelectionField.setObjectName("actionCopySelectionField")
    self.form.menu_Notes.addAction(self.form.actionCopySelectionField)
    qconnect(self.form.actionCopySelectionField.triggered, self.copy_selection_field)


def _update_enabled_actions(self) -> None:
    has_selection = bool(self.table.len_selection())
    self.form.actionCopySelectionField.setEnabled(has_selection)


mw.addonManager.setConfigUpdatedAction(__name__, update_config)

Browser.setupMenus = wrap(Browser.setupMenus, setupMenus, "before")

Browser._update_enabled_actions = wrap(
    Browser._update_enabled_actions, _update_enabled_actions
)

Browser.copy_selection_field = copy_selection_field
