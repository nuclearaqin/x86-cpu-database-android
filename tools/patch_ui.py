# -*- coding: utf-8 -*-
"""Conservative UI polish: spacing, type scale, list behaviour, tablet sizing.

Only resource XML is touched; no class names, ids or interaction logic change.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'decoded'
RES = ROOT / 'res'


def patch(rel, pairs, expect=None):
    p = RES / rel
    txt = p.read_text(encoding='utf-8')
    for old, new, cnt in pairs:
        found = txt.count(old)
        if found != cnt:
            raise SystemExit(f'{rel}: expected {cnt} hits, found {found} for {old[:60]!r}')
        txt = txt.replace(old, new)
    p.write_text(txt, encoding='utf-8')
    print(f'  patched {rel}')


# ---------------------------------------------------------------- 1. dimens
dimen = RES / 'values' / 'dimens.xml'
t = dimen.read_text(encoding='utf-8')
if 'app_nav_width' in t:
    raise SystemExit('dimens already patched')
t = t.replace('</resources>', '''    <dimen name="app_nav_width">304dp</dimen>
    <dimen name="app_breadcrumb_height">42dp</dimen>
    <dimen name="app_list_item_height">52dp</dimen>
    <dimen name="app_list_side_padding">16dp</dimen>
    <dimen name="app_spec_pad_v">6dp</dimen>
    <dimen name="app_detail_header_height">56dp</dimen>
</resources>''')
dimen.write_text(t, encoding='utf-8')
print('  patched values/dimens.xml')

tablet = RES / 'values-sw600dp'
tablet.mkdir(exist_ok=True)
(tablet / 'dimens.xml').write_text('''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <dimen name="app_nav_width">360dp</dimen>
    <dimen name="app_breadcrumb_height">48dp</dimen>
    <dimen name="app_list_item_height">56dp</dimen>
    <dimen name="app_list_side_padding">24dp</dimen>
    <dimen name="app_spec_pad_v">8dp</dimen>
    <dimen name="app_detail_header_height">64dp</dimen>
</resources>
''', encoding='utf-8')
print('  added values-sw600dp/dimens.xml')

# ---------------------------------------------------------------- 2. drawer width
patch('layout/activity_main.xml', [(
    'android:id="@id/navview" android:fitsSystemWindows="true" android:layout_width="wrap_content"',
    'android:id="@id/navview" android:fitsSystemWindows="true" android:layout_width="@dimen/app_nav_width"',
    1)])

# ---------------------------------------------------------------- 3. breadcrumb bars
BREADCRUMBS = [
    'layout/fragment_products.xml', 'layout/fragment_serie_cpu.xml',
    'layout/fragment_list_cpu.xml', 'layout/fragment_search_list_cpu.xml',
    'layout/fragment_top_cpu.xml', 'layout/fragment_favorite_cpu.xml',
    'layout/fragment_history_cpu.xml', 'layout/fragment_list_cpu_comparator.xml',
]
for rel in BREADCRUMBS:
    patch(rel, [
        ('android:textAppearance="?android:textAppearanceSmall" android:ellipsize="start"',
         'android:textAppearance="?android:textAppearanceSmall" android:textSize="13.0sp" '
         'android:textStyle="bold" android:ellipsize="start"', 1),
        ('android:paddingLeft="15.0dp" android:paddingRight="15.0dp" '
         'android:layout_width="match_parent" android:layout_height="40.0dp"',
         'android:paddingLeft="@dimen/app_list_side_padding" '
         'android:paddingRight="@dimen/app_list_side_padding" '
         'android:layout_width="match_parent" android:layout_height="@dimen/app_breadcrumb_height"', 1),
    ])

# ---------------------------------------------------------------- 4. list fills screen
LIST_ATTRS = ('android:divider="@color/grey300" android:dividerHeight="1.0dp" '
              'android:clipToPadding="false" android:paddingBottom="8.0dp" '
              'android:scrollbarStyle="outsideOverlay"')

patch('layout/fragment_products.xml', [
    ('<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="wrap_content"',
     '<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="match_parent"', 1),
    ('android:id="@id/LstProducts" android:layout_width="match_parent" '
     'android:layout_height="wrap_content" />',
     f'android:id="@id/LstProducts" android:layout_width="match_parent" '
     f'android:layout_height="0.0dp" android:layout_weight="1.0" {LIST_ATTRS} />', 1),
])

patch('layout/fragment_serie_cpu.xml', [
    ('<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="wrap_content"',
     '<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="match_parent"', 1),
    ('android:id="@id/LstSeries" android:layout_width="match_parent" '
     'android:layout_height="wrap_content" />',
     f'android:id="@id/LstSeries" android:layout_width="match_parent" '
     f'android:layout_height="0.0dp" android:layout_weight="1.0" {LIST_ATTRS} />', 1),
])

patch('layout/fragment_list_cpu.xml', [
    ('<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="wrap_content"',
     '<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
     'android:layout_height="match_parent"', 1),
    ('android:id="@id/LstCPUs" android:layout_width="match_parent" '
     'android:layout_height="wrap_content" />',
     f'android:id="@id/LstCPUs" android:layout_width="match_parent" '
     f'android:layout_height="0.0dp" android:layout_weight="1.0" {LIST_ATTRS} />', 1),
])

for rel in ('layout/fragment_search_list_cpu.xml', 'layout/fragment_top_cpu.xml',
            'layout/fragment_favorite_cpu.xml', 'layout/fragment_history_cpu.xml'):
    patch(rel, [
        ('<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
         'android:layout_height="wrap_content">',
         '<LinearLayout android:orientation="vertical" android:layout_width="match_parent" '
         'android:layout_height="match_parent">', 1),
        ('android:id="@id/LstCPUs" android:layout_width="match_parent" '
         'android:layout_height="wrap_content" />',
         f'android:id="@id/LstCPUs" android:layout_width="match_parent" '
         f'android:layout_height="0.0dp" android:layout_weight="1.0" {LIST_ATTRS} />', 1),
    ])

patch('layout/fragment_list_cpu_comparator.xml', [
    ('android:layout_height="wrap_content" android:layout_above="@id/linearLayout"',
     'android:layout_height="match_parent" android:layout_above="@id/linearLayout"', 1),
    ('android:id="@id/LstCPUs" android:layout_width="match_parent" '
     'android:layout_height="wrap_content" />',
     f'android:id="@id/LstCPUs" android:layout_width="match_parent" '
     f'android:layout_height="0.0dp" android:layout_weight="1.0" {LIST_ATTRS} />', 1),
])

# ---------------------------------------------------------------- 5. list rows
ROW_TEXT = [
    ('layout/item_list.xml', 1),
    ('layout/item_list_with_star.xml', 1),
    ('layout/item_list_with_trash.xml', 1),
    ('layout/item_list_with_trash_checkable.xml', 1),
    ('layout/item_list_with_compare_and_star.xml', 1),
]
for rel, _ in ROW_TEXT:
    patch(rel, [
        ('android:gravity="center_vertical" android:id="@id/text1"',
         'android:textSize="15.0sp" android:gravity="center_vertical" android:id="@id/text1"', 1),
        ('android:layout_height="wrap_content" android:minHeight="?android:listPreferredItemHeightSmall"',
         'android:layout_height="wrap_content" android:minHeight="@dimen/app_list_item_height" '
         'android:lineSpacingExtra="2.0dp" android:paddingTop="6.0dp" '
         'android:paddingBottom="6.0dp"', 1),
    ])

# ---------------------------------------------------------------- 6. spec rows
patch('layout/item_info_new.xml', [
    ('android:id="@id/specificacionName" android:paddingLeft="16.0dp" android:paddingTop="5.0dp" '
     'android:paddingRight="10.0dp" android:paddingBottom="5.0dp" android:layout_width="0.0dp" '
     'android:layout_height="match_parent" android:text="" android:layout_weight="0.5"',
     'android:id="@id/specificacionName" android:textSize="13.0sp" '
     'android:paddingLeft="@dimen/app_list_side_padding" android:paddingTop="@dimen/app_spec_pad_v" '
     'android:paddingRight="10.0dp" android:paddingBottom="@dimen/app_spec_pad_v" '
     'android:layout_width="0.0dp" android:layout_height="match_parent" android:text="" '
     'android:layout_weight="0.42"', 1),
    ('android:id="@id/specificacionValue" android:paddingLeft="10.0dp" android:paddingTop="5.0dp" '
     'android:paddingRight="16.0dp" android:paddingBottom="5.0dp" android:layout_width="0.0dp" '
     'android:layout_height="match_parent" android:text="" android:layout_weight="0.5"',
     'android:id="@id/specificacionValue" android:textSize="13.0sp" '
     'android:lineSpacingExtra="2.0dp" android:paddingLeft="10.0dp" '
     'android:paddingTop="@dimen/app_spec_pad_v" android:paddingRight="@dimen/app_list_side_padding" '
     'android:paddingBottom="@dimen/app_spec_pad_v" android:layout_width="0.0dp" '
     'android:layout_height="match_parent" android:text="" android:layout_weight="0.58"', 1),
])

patch('layout/item_info_group.xml', [
    ('android:gravity="center" android:id="@id/groupName" android:paddingLeft="?android:expandableListPreferredChildPaddingLeft" android:paddingTop="6.0dp"',
     'android:textSize="14.0sp" android:gravity="center_vertical" android:id="@id/groupName" '
     'android:paddingLeft="@dimen/app_list_side_padding" android:paddingTop="8.0dp"', 1),
    ('android:paddingRight="?android:expandableListPreferredItemPaddingLeft" android:paddingBottom="6.0dp"',
     'android:paddingRight="@dimen/app_list_side_padding" android:paddingBottom="8.0dp"', 1),
])

# ---------------------------------------------------------------- 7. detail header
patch('layout/fragment_info_cpu.xml', [
    ('android:background="@color/teal1" android:layout_width="match_parent" android:layout_height="50.0dp"',
     'android:background="@color/teal1" android:layout_width="match_parent" '
     'android:layout_height="@dimen/app_detail_header_height"', 1),
    ('android:id="@id/iconCPU" android:padding="5.0dp" android:layout_width="50.0dp" '
     'android:layout_height="50.0dp"',
     'android:id="@id/iconCPU" android:padding="7.0dp" android:layout_width="@dimen/app_detail_header_height" '
     'android:layout_height="@dimen/app_detail_header_height"', 1),
    ('android:textSize="20.0sp" android:textStyle="bold" android:textColor="@color/white" '
     'android:ellipsize="end" android:gravity="center_vertical" android:id="@id/nameCPUText" '
     'android:paddingLeft="10.0dp" android:layout_width="match_parent" '
     'android:layout_height="match_parent"',
     'android:textSize="19.0sp" android:textStyle="bold" android:textColor="@color/white" '
     'android:ellipsize="end" android:maxLines="2" android:gravity="center_vertical" '
     'android:id="@id/nameCPUText" android:paddingLeft="6.0dp" android:paddingRight="10.0dp" '
     'android:layout_width="match_parent" android:layout_height="match_parent"', 1),
])

print('UI patch complete')
