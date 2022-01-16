# Anki copy selection field

An Anki add-on for copying all the fields of a selection in the browse
window.

**Addon URL**: <https://ankiweb.net/shared/info/1726946295>

**Addon Code**: `1726946295`

### Example

![image](https://user-images.githubusercontent.com/3298461/149669228-50015b6d-9aff-447f-8fcf-afcf5e2e8ab1.png)

with the default options will paste the following:

```
analytic
convenience
efficiency
supposed to
as an
```

> ⚠️  Output might not be in the same order as on the browse window
> ([#1](https://github.com/antistic/anki-copy-selection-field/issues/1))

## Usage

1. Open the browse window
2. Make a selection
3. Press `ctrl+shift+c`, or choose from the "Notes" menu (also available in
   the right click context menu)
4. Paste the text wherever you want

## Options

| Option | Default Value | Description |
| ------ | ------------- | ----------- |
| `field_index` | `0` | (int) The index of the field you want to copy. The first field is number `0` |
| `separator` | `"\n"` | (string) What goes in between each note |
| `strip_html` | `true` | (bool) Whether or not to strip html tags (e.g. `<div>`, `<strong>`) |
