from __future__ import unicode_literals

from django.utils.six.moves import zip_longest
from djblets.cache.backend import cache_memoize
import nose
from reviewboard.admin.import_utils import has_module
from reviewboard.diffviewer.processors import (filter_interdiff_opcodes,
                                               post_process_filtered_equals)
from reviewboard.scmtools.core import PRE_CREATION
from reviewboard.testing import TestCase
    def test_diff(self):
        """Testing MyersDiffer"""
        self._test_diff(["1", "2", "3"],
                        ["1", "2", "3"],
                        [("equal", 0, 3, 0, 3), ])

        self._test_diff(["1", "2", "3"],
                        [],
                        [("delete", 0, 3, 0, 0), ])

        self._test_diff("1\n2\n3\n",
                        "0\n1\n2\n3\n",
                        [("insert", 0, 0, 0, 2),
                         ("equal", 0, 6, 2, 8)])

        self._test_diff("1\n2\n3\n7\n",
                        "1\n2\n4\n5\n6\n7\n",
                        [("equal", 0, 4, 0, 4),
                         ("replace", 4, 5, 4, 5),
                         ("insert", 5, 5, 5, 9),
                         ("equal", 5, 8, 9, 12)])

    def _test_diff(self, a, b, expected):
    def test_csharp(self):
        lines = self._get_lines("helloworld.cs")
    def test_java(self):
        lines = self._get_lines("helloworld.java")
    def test_javascript(self):
        lines = self._get_lines("helloworld.js")
    def test_objective_c(self):
        lines = self._get_lines("helloworld.m")
    def test_perl(self):
        lines = self._get_lines("helloworld.pl")
    def test_php(self):
        lines = self._get_lines("helloworld.php")
        self.assertEqual(len(lines[1]), 3)
        self.assertEqual(lines[1][2], (14, '\tpublic function foo() {\n'))
    def test_python(self):
        lines = self._get_lines("helloworld.py")
    def test_ruby(self):
        lines = self._get_lines("helloworld.rb")
    def _get_lines(self, filename):
        with open(os.path.join(self.PREFIX, "orig_src", filename), "r") as f:
            a = f.readlines()
        with open(os.path.join(self.PREFIX, "new_src", filename), "r") as f:
            b = f.readlines()
class DiffParserTest(TestCase):
    def _compare_diffs(self, files, testdir):
            self.assertTrue(file.origFile.startswith("%s/orig_src/" %
            self.assertTrue(file.newFile.startswith("%s/new_src/" %
    def test_unified_diff(self):
        """Testing DiffParser.parse on a unified diff"""
        self._compare_diffs(files, "unified")
    def test_context_diff(self):
        """Testing DiffParser.parse on a context diff"""
        self._compare_diffs(files, "context")
    def test_patch(self):
        """Testing diffutils.patch"""
    def test_empty_patch(self):
        """Testing diffutils.patch with an empty diff"""
    def test_patch_crlf_file_crlf_diff(self):
        """Testing diffutils.patch with a CRLF file and a CRLF diff"""
    def test_patch_cr_file_crlf_diff(self):
        """Testing diffutils.patch with a CR file and a CRLF diff"""
    def test_patch_crlf_file_cr_diff(self):
        """Testing diffutils.patch with a CRLF file and a CR diff"""
    def test_patch_file_with_fake_no_newline(self):
        """Testing diffutils.patch with a file indicating no newline
        with a trailing \\r
        """
    def test_move_detection(self):
        """Testing diff viewer move detection"""
        self._test_move_detection(
            old.splitlines(),
            new.splitlines(),
            [
                {
                    28: 15,
                    29: 16,
                    30: 17,
                    31: 18,
                }
            ],
            [
                {
                    15: 28,
                    16: 29,
                    17: 30,
                    18: 31,
                }
            ])

    def test_move_detection_with_replace_lines(self):
        """Testing diff viewer move detection with replace lines"""
        self._test_move_detection(
            [
                'this is line 1, and it is sufficiently long',
                '-------------------------------------------',
                '-------------------------------------------',
                'this is line 2, and it is sufficiently long',
            ],
            [
                'this is line 2, and it is sufficiently long',
                '-------------------------------------------',
                '-------------------------------------------',
                'this is line 1, and it is sufficiently long',
            ],
            [
                {1: 4},
                {4: 1},
            ],
            [
                {1: 4},
                {4: 1},
            ]
        )
    def test_move_detection_with_whitespace_replace_lines(self):
        """Testing diff viewer move detection with whitespace-only
        changes on replace lines
        """
        self._test_move_detection(
            [
                'this is line 1, and it is sufficiently long',
                '-------------------------------------------',
                '-------------------------------------------',
                'this is line 2, and it is sufficiently long  ',
            ],
            [
                '  this is line 1, and it is sufficiently long',
                '-------------------------------------------',
                '-------------------------------------------',
                'this is line 2, and it is sufficiently long',
            ],
            [],
            []
        )

    def test_move_detection_with_last_line_in_range(self):
        """Testing diff viewer move detection with last line in a range"""
        # The move detection rewrite in 2.0 introduced an off-by-one where
        # the last line in a chunk wasn't being processed as a move unless
        # the line after the chunk had content. That line should never have
        # been processed either.
        self._test_move_detection(
            [
                'this line will be replaced',
                '',
                'foo bar blah blah',
                'this is line 1, and it is sufficiently long',
                '',
            ],
            [
                'this is line 1, and it is sufficiently long',
                '',
                'foo bar blah blah',
                '',
            ],
            [
                {1: 4},
            ],
            [
                {4: 1},
            ]
        )

    def test_move_detection_with_adjacent_regions(self):
        """Testing diff viewer move detection with adjacent regions"""
        self._test_move_detection(
            [
                '1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                '2. Phasellus et lectus vulputate, dictum mi id, auctor ante.',
                '3. Nulla accumsan tellus ut felis ultrices euismod.',
                '4. Donec quis augue sed arcu tristique pellentesque.',
                '5. Fusce rutrum diam vel viverra sagittis.',
                '6. Nam tincidunt sapien vitae lorem vestibulum tempor.',
                '7. Donec fermentum tortor ut egestas convallis.',
            ],
            [
                '6. Nam tincidunt sapien vitae lorem vestibulum tempor.',
                '7. Donec fermentum tortor ut egestas convallis.',
                '4. Donec quis augue sed arcu tristique pellentesque.',
                '5. Fusce rutrum diam vel viverra sagittis.',
                '1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                '2. Phasellus et lectus vulputate, dictum mi id, auctor ante.',
                '3. Nulla accumsan tellus ut felis ultrices euismod.',
            ],
            [
                {
                    1: 6,
                    2: 7,
                    3: 4,
                    4: 5,
                }
            ],
            [
                {
                    4: 3,
                    5: 4,
                    6: 1,
                    7: 2,
                }
            ],
        )

    def test_move_detection_spanning_chunks(self):
        """Testing diff viewer move detection spanning left-hand-side chunks"""
        # This is testing an insert move range (the first 4 lines on the
        # second list of lines) that spans 3 chunks (1 replace line, 1 equal
        # blank line, and 2 delete lines).
        self._test_move_detection(
            [
                'Unchanged line 1',
                'Unchanged line 2',
                'Unchanged line 3',
                'Unchanged line 4',
                '====',
                'this is line 1, and it is sufficiently long',
                '',
                'this is line 2, and it is sufficiently long',
                'this is line 3, and it is sufficiently long',
                '',
            ],
            [
                'this is line 1, and it is sufficiently long',
                '',
                'this is line 2, and it is sufficiently long',
                'this is line 3, and it is sufficiently long',
                'Unchanged line 1',
                'Unchanged line 2',
                'Unchanged line 3',
                'Unchanged line 4',
                '====',
                'this is line X, and it is sufficiently long',
                '',
                '',
            ],
            [
                {
                    1: 6,
                    2: 7,
                    3: 8,
                    4: 9,
                },
            ],
            [
                # The entire move range is stored for every chunk, hence
                # the repeats.
                {
                    6: 1,
                    7: 2,
                    8: 3,
                    9: 4,
                },
                {
                    6: 1,
                    7: 2,
                    8: 3,
                    9: 4,
                },
                {
                    6: 1,
                    7: 2,
                    8: 3,
                    9: 4,
                },
            ]
        )

    def test_move_detection_single_line_thresholds(self):
        """Testing diff viewer move detection with a single line and
        line length threshold
        """
        self._test_move_detection(
            [
                '0123456789012345678',
                '----',
                '----',
                'abcdefghijklmnopqrst',
            ],
            [
                'abcdefghijklmnopqrst',
                '----',
                '----',
                '0123456789012345678',
            ],
            [
                {1: 4},
            ],
            [
                {4: 1},
            ]
        )

    def test_move_detection_multi_line_thresholds(self):
        """Testing diff viewer move detection with a multiple lines and
        line count threshold
        """
        self._test_move_detection(
            [
                '123',
                '456',
                '789',
                'ten',
                'abcdefghijk',
                'lmno',
                'pqr',
            ],
            [
                'abcdefghijk',
                'lmno',
                'pqr',
                '123',
                '456',
                '789',
                'ten',
            ],
            [
                {
                    1: 5,
                    2: 6,
                },
            ],
            [
                {
                    5: 1,
                    6: 2,
                },
            ]
        )

    def test_line_counts(self):
        """Testing DiffParser with insert/delete line counts"""
        diff = (
            b'+ This is some line before the change\n'
            b'- And another line\n'
            b'Index: foo\n'
            b'- One last.\n'
            b'--- README  123\n'
            b'+++ README  (new)\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah blah\n'
            b'-blah\n'
            b'+blah!\n'
            b'-blah...\n'
            b'+blah?\n'
            b'-blah!\n'
            b'+blah?!\n')
        files = diffparser.DiffParser(diff).parse()

        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].insert_count, 3)
        self.assertEqual(files[0].delete_count, 4)

    def _get_file(self, *relative):
        path = os.path.join(*tuple([self.PREFIX] + list(relative)))
        with open(path, 'rb') as f:
            return f.read()

    def _test_move_detection(self, a, b, expected_i_moves, expected_r_moves):
        differ = MyersDiffer(a, b)
        r_moves = []
        i_moves = []

            if 'moved-to' in meta:
                r_moves.append(meta['moved-to'])
            if 'moved-from' in meta:
                i_moves.append(meta['moved-from'])

        self.assertEqual(i_moves, expected_i_moves)
        self.assertEqual(r_moves, expected_r_moves)

class FileDiffTests(TestCase):
    """Unit tests for FileDiff."""
    fixtures = ['test_scmtools']

    def setUp(self):
        super(FileDiffTests, self).setUp()

        diff = (
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,2 @@\n'
            b'-blah blah\n'
            b'+blah!\n'
            b'+blah!!\n')

        repository = self.create_repository(tool_name='Test')
        diffset = DiffSet.objects.create(name='test',
                                         revision=1,
                                         repository=repository)
        self.filediff = FileDiff(source_file='README',
                                 dest_file='README',
                                 diffset=diffset,
                                 diff64=diff,
                                 parent_diff64='')

    def test_get_line_counts_with_defaults(self):
        """Testing FileDiff.get_line_counts with default values"""
        counts = self.filediff.get_line_counts()

        self.assertIn('raw_insert_count', counts)
        self.assertIn('raw_delete_count', counts)
        self.assertIn('insert_count', counts)
        self.assertIn('delete_count', counts)
        self.assertIn('replace_count', counts)
        self.assertIn('equal_count', counts)
        self.assertIn('total_line_count', counts)
        self.assertEqual(counts['raw_insert_count'], 2)
        self.assertEqual(counts['raw_delete_count'], 1)
        self.assertEqual(counts['insert_count'], 2)
        self.assertEqual(counts['delete_count'], 1)
        self.assertIsNone(counts['replace_count'])
        self.assertIsNone(counts['equal_count'])
        self.assertIsNone(counts['total_line_count'])

        diff_hash = self.filediff.diff_hash
        self.assertEqual(diff_hash.insert_count, 2)
        self.assertEqual(diff_hash.delete_count, 1)

    def test_set_line_counts(self):
        """Testing FileDiff.set_line_counts"""
        self.filediff.set_line_counts(
            raw_insert_count=1,
            raw_delete_count=2,
            insert_count=3,
            delete_count=4,
            replace_count=5,
            equal_count=6,
            total_line_count=7)

        counts = self.filediff.get_line_counts()
        self.assertEqual(counts['raw_insert_count'], 1)
        self.assertEqual(counts['raw_delete_count'], 2)
        self.assertEqual(counts['insert_count'], 3)
        self.assertEqual(counts['delete_count'], 4)
        self.assertEqual(counts['replace_count'], 5)
        self.assertEqual(counts['equal_count'], 6)
        self.assertEqual(counts['total_line_count'], 7)

        diff_hash = self.filediff.diff_hash
        self.assertEqual(diff_hash.insert_count, 1)
        self.assertEqual(diff_hash.delete_count, 2)


class FileDiffMigrationTests(TestCase):
    fixtures = ['test_scmtools']

    def setUp(self):
        super(FileDiffMigrationTests, self).setUp()

        self.diff = (
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah blah\n'
            b'+blah!\n')
        self.parent_diff = (
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah..\n'
            b'+blah blah\n')

        repository = self.create_repository(tool_name='Test')
        diffset = DiffSet.objects.create(name='test',
                                         revision=1,
                                         repository=repository)
        self.filediff = FileDiff(source_file='README',
                                 dest_file='README',
                                 diffset=diffset,
                                 diff64='',
                                 parent_diff64='')

    def test_migration_by_diff(self):
        """Testing FileDiffData migration accessing FileDiff.diff"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)
        self.assertEqual(self.filediff.parent_diff_hash, None)

        # This should prompt the migration
        diff = self.filediff.diff

        self.assertEqual(self.filediff.parent_diff_hash, None)
        self.assertNotEqual(self.filediff.diff_hash, None)

        self.assertEqual(diff, self.diff)
        self.assertEqual(self.filediff.diff64, '')
        self.assertEqual(self.filediff.diff_hash.binary, self.diff)
        self.assertEqual(self.filediff.diff, diff)
        self.assertEqual(self.filediff.parent_diff, None)
        self.assertEqual(self.filediff.parent_diff_hash, None)

    def test_migration_by_parent_diff(self):
        """Testing FileDiffData migration accessing FileDiff.parent_diff"""
        self.filediff.diff64 = self.diff
        self.filediff.parent_diff64 = self.parent_diff

        self.assertEqual(self.filediff.parent_diff_hash, None)

        # This should prompt the migration
        parent_diff = self.filediff.parent_diff

        self.assertNotEqual(self.filediff.parent_diff_hash, None)

        self.assertEqual(parent_diff, self.parent_diff)
        self.assertEqual(self.filediff.parent_diff64, '')
        self.assertEqual(self.filediff.parent_diff_hash.binary,
                         self.parent_diff)
        self.assertEqual(self.filediff.parent_diff, self.parent_diff)

    def test_migration_by_delete_count(self):
        """Testing FileDiffData migration accessing FileDiff.delete_count"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration
        counts = self.filediff.get_line_counts()

        self.assertNotEqual(self.filediff.diff_hash, None)
        self.assertEqual(counts['raw_delete_count'], 1)
        self.assertEqual(self.filediff.diff_hash.delete_count, 1)

    def test_migration_by_insert_count(self):
        """Testing FileDiffData migration accessing FileDiff.insert_count"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration
        counts = self.filediff.get_line_counts()

        self.assertNotEqual(self.filediff.diff_hash, None)
        self.assertEqual(counts['raw_insert_count'], 1)
        self.assertEqual(self.filediff.diff_hash.insert_count, 1)

    def test_migration_by_set_line_counts(self):
        """Testing FileDiffData migration calling FileDiff.set_line_counts"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration, but with our line counts.
        self.filediff.set_line_counts(raw_insert_count=10,
                                      raw_delete_count=20)

        self.assertNotEqual(self.filediff.diff_hash, None)

        counts = self.filediff.get_line_counts()
        self.assertEqual(counts['raw_insert_count'], 10)
        self.assertEqual(counts['raw_delete_count'], 20)
        self.assertEqual(self.filediff.diff_hash.insert_count, 10)
        self.assertEqual(self.filediff.diff_hash.delete_count, 20)
        repository = self.create_repository()
        super(HighlightRegionTest, self).setUp()

    def test_highlight_region(self):
                          '<span class="hl">abc</span>')
                          '<span class="hl">a</span>bc')
        repository = self.create_repository()
        repository = self.create_repository()
        with open(os.path.join(self.PREFIX, "diffs", "context",
                               "foo.c.diff")) as f:
            data = f.read()
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah..\n'
            b'+blah blah\n'
        repository = self.create_repository(tool_name='Test')
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah..\n'
            b'+blah blah\n'
        repository = self.create_repository(tool_name='Test')
            b'diff --git a/README b/README\n'
            b'index d6613f5..5b50866 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah blah\n'
            b'+blah!\n'
            b'diff --git a/README b/README\n'
            b'index d6613f4..5b50865 100644\n'
            b'--- README\n'
            b'+++ README\n'
            b'@ -1,1 +1,1 @@\n'
            b'-blah..\n'
            b'+blah blah\n'
            b'diff --git a/UNUSED b/UNUSED\n'
            b'index 1234567..5b50866 100644\n'
            b'--- UNUSED\n'
            b'+++ UNUSED\n'
            b'@ -1,1 +1,1 @@\n'
            b'-foo\n'
            b'+bar\n'
        repository = self.create_repository(tool_name='Test')
        self.assertIn(('/README', 'd6613f4'), saw_file_exists)
        self.assertNotIn(('/UNUSED', '1234567'), saw_file_exists)
        """Testing that the correct base revision is used for Mercurial diffs
        """
            b'# Node ID a6fc203fee9091ff9739c9c00cd4a6694e023f48\n'
            b'# Parent  7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            b'diff --git a/doc/readme b/doc/readme\n'
            b'--- a/doc/readme\n'
            b'+++ b/doc/readme\n'
            b'@@ -1,3 +1,3 @@\n'
            b' Hello\n'
            b'-\n'
            b'+...\n'
            b' goodbye\n'
            b'# Node ID 7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            b'# Parent  661e5dd3c4938ecbe8f77e2fdfa905d70485f94c\n'
            b'diff --git a/doc/newfile b/doc/newfile\n'
            b'new file mode 100644\n'
            b'--- /dev/null\n'
            b'+++ b/doc/newfile\n'
            b'@@ -0,0 +1,1 @@\n'
            b'+Lorem ipsum\n'
        if not has_module('mercurial'):
            raise nose.SkipTest("Hg is not installed")

class ProcessorsTests(TestCase):
    """Unit tests for diff processors."""

    def test_filter_interdiff_opcodes(self):
        """Testing filter_interdiff_opcodes"""
        opcodes = [
            ('insert', 0, 0, 0, 1),
            ('equal', 0, 5, 1, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 21),
            ('equal', 26, 40, 21, 35),
            ('insert', 40, 40, 35, 45),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = (
            '@@ -22,7 +22,7 @@\n'
            ' #\n #\n #\n-#\n'
        )
        new_diff = (
            '@@ -2,11 +2,6 @@\n'
            ' #\n #\n #\n-#\n'
            '@@ -22,7 +22,7 @@\n'
            ' #\n #\n #\n-#\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('filtered-equal', 0, 0, 0, 1),
            ('filtered-equal', 0, 5, 1, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 21),
            ('equal', 26, 32, 21, 27),
            ('filtered-equal', 32, 40, 27, 35),
            ('filtered-equal', 40, 40, 35, 45),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_replace_after_valid_ranges(self):
        """Testing filter_interdiff_opcodes with replace after valid range"""
        # While developing the fix for replace lines in
        # https://reviews.reviewboard.org/r/6030/, an iteration of the fix
        # broke replace lines when one side exceeded its last range found in
        # the diff.
        opcodes = [
            ('replace', 12, 13, 5, 6),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = (
            '@@ -2,7 +2,7 @@\n'
            ' #\n #\n #\n-#\n'
        )
        new_diff = (
            '@@ -2,7 +2,7 @@\n'
            ' #\n #\n #\n-#\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('replace', 12, 13, 5, 6),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_1_line(self):
        """Testing filter_interdiff_opcodes with a 1 line file"""
        opcodes = [
            ('replace', 0, 1, 0, 1),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = (
            '@@ -0,0 +1 @@\n'
            '+#\n'
        )
        new_diff = (
            '@@ -0,0 +1 @@\n'
            '+##\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('replace', 0, 1, 0, 1),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_early_change(self):
        """Testing filter_interdiff_opcodes with a change early in the file"""
        opcodes = [
            ('replace', 2, 3, 2, 3),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = (
            '@@ -1,5 +1,5 @@\n'
            ' #\n#\n+#\n'
        )
        new_diff = (
            '@@ -1,5 +1,5 @@\n'
            ' #\n#\n+#\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('replace', 2, 3, 2, 3),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_with_inserts_right(self):
        """Testing filter_interdiff_opcodes with inserts on the right"""
        # These opcodes were taken from the r1-r2 interdiff at
        # http://reviews.reviewboard.org/r/4221/
        opcodes = [
            ('equal', 0, 141, 0, 141),
            ('replace', 141, 142, 141, 142),
            ('insert', 142, 142, 142, 144),
            ('equal', 142, 165, 144, 167),
            ('replace', 165, 166, 167, 168),
            ('insert', 166, 166, 168, 170),
            ('equal', 166, 190, 170, 194),
            ('insert', 190, 190, 194, 197),
            ('equal', 190, 232, 197, 239),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = (
            '@@ -0,0 +1,232 @@\n'
            ' #\n #\n #\n+#\n'
        )
        new_diff = (
            '@@ -0,0 +1,239 @@\n'
            ' #\n #\n #\n+#\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('filtered-equal', 0, 141, 0, 141),
            ('replace', 141, 142, 141, 142),
            ('insert', 142, 142, 142, 144),
            ('equal', 142, 165, 144, 167),
            ('replace', 165, 166, 167, 168),
            ('insert', 166, 166, 168, 170),
            ('equal', 166, 190, 170, 194),
            ('insert', 190, 190, 194, 197),
            ('equal', 190, 232, 197, 239),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_with_many_ignorable_ranges(self):
        """Testing filter_interdiff_opcodes with many ignorable ranges"""
        # These opcodes were taken from the r1-r2 interdiff at
        # http://reviews.reviewboard.org/r/4257/
        opcodes = [
            ('equal', 0, 631, 0, 631),
            ('replace', 631, 632, 631, 632),
            ('insert', 632, 632, 632, 633),
            ('equal', 632, 882, 633, 883),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = '\n'.join([
            '@@ -413,6 +413,8 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -422,9 +424,13 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -433,6 +439,8 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -442,6 +450,9 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -595,6 +605,205 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -636,6 +845,36 @@\n'
            ' #\n #\n #\n+#\n'
        ])
        new_diff = '\n'.join([
            '@@ -413,6 +413,8 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -422,9 +424,13 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -433,6 +439,8 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -442,6 +450,8 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -595,6 +605,206 @@\n'
            ' #\n #\n #\n+#\n'
            '@@ -636,6 +846,36 @@\n'
            ' #\n #\n #\n+#\n'
        ])

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('filtered-equal', 0, 631, 0, 631),
            ('replace', 631, 632, 631, 632),
            ('insert', 632, 632, 632, 633),
            ('equal', 632, 813, 633, 814),
            ('filtered-equal', 813, 882, 814, 883),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_filter_interdiff_opcodes_with_replace_overflowing_range(self):
        """Testing filter_interdiff_opcodes with replace overflowing range"""
        # In the case where there's a replace chunk with i2 or j2 larger than
        # the end position of the current range, the chunk would get chopped,
        # and the two replace ranges could be unequal. This broke an assertion
        # check when generating opcode metadata, and would result in a
        # corrupt-looking diff.
        #
        # This is bug #3440
        #
        # Before the fix, the below opcodes and diff ranges would result
        # in the replace turning into (2, 6, 2, 15), instead of staying at
        # (2, 15, 2, 15).
        #
        # This only really tends to happen in early ranges (since the range
        # numbers are small), but could also happen further into the diff
        # if a replace range is huge on one side.
        opcodes = [
            ('equal', 0, 2, 0, 2),
            ('replace', 2, 100, 2, 100),
        ]
        self._sanity_check_opcodes(opcodes)

        # NOTE: Only the "@@" lines and the lines leading up to the first
        #       change in a chunk matter to the processor, so the rest can
        #       be left out.
        orig_diff = ''.join([
            '@@ -1,4 +1,5 @@\n',
            '-#\n',
            '@@ -8,18 +9,19 @\n'
            ' #\n #\n #\n+#\n',
        ])
        new_diff = ''.join([
            '@@ -1,10 +1,14 @@\n'
            '-#\n',
        ])

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('equal', 0, 2, 0, 2),
            ('replace', 2, 15, 2, 15),
            ('filtered-equal', 15, 100, 15, 100),
        ])
        self._sanity_check_opcodes(new_opcodes)

    def test_post_process_filtered_equals(self):
        """Testing post_process_filtered_equals"""
        opcodes = [
            ('equal', 0, 10, 0, 10, {}),
            ('insert', 10, 20, 0, 10, {}),
            ('equal', 20, 30, 10, 20, {}),
            ('equal', 30, 40, 20, 30, {}),
            ('filtered-equal', 40, 50, 30, 40, {}),
        ]

        new_opcodes = list(post_process_filtered_equals(opcodes))

        self.assertEqual(
            new_opcodes,
            [
                ('equal', 0, 10, 0, 10, {}),
                ('insert', 10, 20, 0, 10, {}),
                ('equal', 20, 50, 10, 40, {}),
            ])

    def test_post_process_filtered_equals_with_indentation(self):
        """Testing post_process_filtered_equals with indentation changes"""
        opcodes = [
            ('equal', 0, 10, 0, 10, {}),
            ('insert', 10, 20, 0, 10, {}),
            ('equal', 20, 30, 10, 20, {
                'indentation_changes': {
                    '21-11': (True, 4),
                }
            }),
            ('equal', 30, 40, 20, 30, {}),
            ('filtered-equal', 30, 50, 20, 40, {}),
        ]

        new_opcodes = list(post_process_filtered_equals(opcodes))

        self.assertEqual(
            new_opcodes,
            [
                ('equal', 0, 10, 0, 10, {}),
                ('insert', 10, 20, 0, 10, {}),
                ('equal', 20, 30, 10, 20, {
                    'indentation_changes': {
                        '21-11': (True, 4),
                    }
                }),
                ('equal', 30, 50, 20, 40, {}),
            ])

    def test_post_process_filtered_equals_with_adjacent_indentation(self):
        """Testing post_process_filtered_equals with
        adjacent indentation changes
        """
        opcodes = [
            ('equal', 0, 10, 0, 10, {}),
            ('insert', 10, 20, 0, 10, {}),
            ('equal', 20, 30, 10, 20, {
                'indentation_changes': {
                    '21-11': (True, 4),
                }
            }),
            ('equal', 30, 40, 20, 30, {
                'indentation_changes': {
                    '31-21': (False, 8),
                }
            }),
            ('filtered-equal', 40, 50, 30, 40, {}),
        ]

        new_opcodes = list(post_process_filtered_equals(opcodes))

        self.assertEqual(
            new_opcodes,
            [
                ('equal', 0, 10, 0, 10, {}),
                ('insert', 10, 20, 0, 10, {}),
                ('equal', 20, 30, 10, 20, {
                    'indentation_changes': {
                        '21-11': (True, 4),
                    }
                }),
                ('equal', 30, 40, 20, 30, {
                    'indentation_changes': {
                        '31-21': (False, 8),
                    }
                }),
                ('equal', 40, 50, 30, 40, {}),
            ])

    def _sanity_check_opcodes(self, opcodes):
        prev_i2 = None
        prev_j2 = None

        for tag, i1, i2, j1, j2 in opcodes:
            if tag == 'replace':
                self.assertEqual((i2 - i1), (j2 - j1))

            if prev_i2 is not None and prev_j2 is not None:
                self.assertEqual(i1, prev_i2)
                self.assertEqual(j1, prev_j2)

            prev_i2 = i2
            prev_j2 = j2


    fixtures = ['test_scmtools']
    def setUp(self):
        self.repository = self.create_repository()
        self.diffset = self.create_diffset(repository=self.repository)
        self.filediff = self.create_filediff(diffset=self.diffset)
        self.generator = DiffChunkGenerator(None, self.filediff)

    def test_get_chunks_with_empty_added_file(self):
        """Testing DiffChunkGenerator.get_chunks with empty added file"""
        self.filediff.source_revision = PRE_CREATION
        self.filediff.extra_data.update({
            'raw_insert_count': 0,
            'raw_delete_count': 0,
        })

        self.assertEqual(len(self.generator.get_chunks()), 0)

    def test_get_chunks_with_replace_in_added_file_with_parent_diff(self):
        """Testing DiffChunkGenerator.get_chunks with replace chunks in
        added file with parent diff
        """
        self.filediff.diff = (
            b'--- README\n'
            b'+++ README\n'
            b'@@ -1,1 +1,1 @@\n'
            b'-line\n'
            b'+line.\n'
        )
        self.filediff.parent_diff = (
            b'--- README\n'
            b'+++ README\n'
            b'@@ -0,0 +1,1 @@\n'
            b'+line\n'
        )
        self.filediff.source_revision = PRE_CREATION
        self.filediff.extra_data.update({
            'raw_insert_count': 1,
            'raw_delete_count': 1,
            'insert_count': 0,
            'delete_count': 0,
        })

        self.assertEqual(len(self.generator.get_chunks()), 1)

    def test_indent_spaces(self):
        """Testing DiffChunkGenerator._serialize_indentation with spaces"""
        self.assertEqual(
            self.generator._serialize_indentation('    ', 4),
            ('&gt;&gt;&gt;&gt;', ''))

    def test_indent_tabs(self):
        """Testing DiffChunkGenerator._serialize_indentation with tabs"""
        self.assertEqual(
            self.generator._serialize_indentation('\t', 8),
            ('&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&gt;|', ''))

    def test_indent_spaces_and_tabs(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with spaces and tabs
        """
        self.assertEqual(
            self.generator._serialize_indentation('   \t', 8),
            ('&gt;&gt;&gt;&mdash;&mdash;&mdash;&gt;|', ''))
    def test_indent_tabs_and_spaces(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with tabs and spaces
        """
        self.assertEqual(
            self.generator._serialize_indentation('\t   ', 11),
            ('&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&gt;|&gt;&gt;&gt;',
             ''))

    def test_indent_9_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 9 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('       \t', 8),
            ('&gt;&gt;&gt;&gt;&gt;&gt;&gt;|', ''))
    def test_indent_8_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 8 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('      \t', 8),
            ('&gt;&gt;&gt;&gt;&gt;&gt;&gt;|', ''))
    def test_indent_7_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 7 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('     \t', 8),
            ('&gt;&gt;&gt;&gt;&gt;&mdash;&gt;|', ''))

    def test_unindent_spaces(self):
        """Testing DiffChunkGenerator._serialize_unindentation with spaces"""
        self.assertEqual(
            self.generator._serialize_unindentation('    ', 4),
            ('&lt;&lt;&lt;&lt;', ''))

    def test_unindent_tabs(self):
        """Testing DiffChunkGenerator._serialize_unindentation with tabs"""
        self.assertEqual(
            self.generator._serialize_unindentation('\t', 8),
            ('|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;', ''))

    def test_unindent_spaces_and_tabs(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with spaces and tabs
        """
        self.assertEqual(
            self.generator._serialize_unindentation('   \t', 8),
            ('&lt;&lt;&lt;|&lt;&mdash;&mdash;&mdash;', ''))
    def test_unindent_tabs_and_spaces(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with tabs and spaces
        """
        self.assertEqual(
            self.generator._serialize_unindentation('\t   ', 11),
            ('|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&lt;&lt;&lt;',
             ''))

    def test_unindent_9_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 9 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('       \t', 8),
            ('&lt;&lt;&lt;&lt;&lt;&lt;&lt;|', ''))

    def test_unindent_8_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 8 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('      \t', 8),
            ('&lt;&lt;&lt;&lt;&lt;&lt;|&lt;', ''))

    def test_unindent_7_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 7 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('     \t', 8),
            ('&lt;&lt;&lt;&lt;&lt;|&lt;&mdash;', ''))

    def test_highlight_indent(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with indentation
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '',
                '        foo',
                True, 4, 4),
            ('', '<span class="indent">&gt;&gt;&gt;&gt;</span>    foo'))

    def test_highlight_indent_with_adjacent_tag(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with indentation and adjacent tag wrapping whitespace
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '',
                '<span class="s"> </span>foo',
                True, 1, 1),
            ('',
             '<span class="s"><span class="indent">&gt;</span></span>foo'))

    def test_highlight_indent_with_unexpected_chars(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with indentation and unexpected markup chars
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '',
                ' <span>  </span> foo',
                True, 4, 2),
            ('', ' <span>  </span> foo'))

    def test_highlight_unindent(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '        foo',
                '',
                False, 4, 4),
            ('<span class="unindent">&lt;&lt;&lt;&lt;</span>    foo', ''))

    def test_highlight_unindent_with_adjacent_tag(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation and adjacent tag wrapping whitespace
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '<span class="s"> </span>foo',
                '',
                False, 1, 1),
            ('<span class="s"><span class="unindent">&lt;</span></span>foo',
             ''))

    def test_highlight_unindent_with_unexpected_chars(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation and unexpected markup chars
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                ' <span>  </span> foo',
                '',
                False, 4, 2),
            (' <span>  </span> foo', ''))

    def test_highlight_unindent_with_replacing_last_tab_with_spaces(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation and replacing last tab with spaces
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '<span>\t\t        </span> foo',
                '',
                False, 2, 16),
            ('<span><span class="unindent">'
             '|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;'
             '|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;'
             '</span>        </span> foo', ''))

    def test_highlight_unindent_with_replacing_3_tabs_with_tab_spaces(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation and replacing 3 tabs with 1 tab and 8 spaces
        """
        self.assertEqual(
            self.generator._highlight_indentation(
                '<span>\t        </span> foo',
                '',
                False, 1, 24),
            ('<span><span class="unindent">'
             '|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;'
             '</span>        </span> foo', ''))


class DiffOpcodeGeneratorTests(TestCase):
    """Unit tests for DiffOpcodeGenerator."""
    def setUp(self):
        self.generator = get_diff_opcode_generator(MyersDiffer('', ''))

    def test_indentation_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '        foo'),
            (True, 4, 4))

    def test_indentation_with_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '\t    foo'),
            (True, 1, 8))

    def test_indentation_with_spaces_and_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting spaces and tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '  \t    foo'),
            (True, 3, 8))

    def test_indentation_with_tabs_and_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting tabs and spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '\t      foo'),
            (True, 3, 10))

    def test_indentation_with_replacing_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with replacing tabs with spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\tfoo',
                '        foo'),
            None)

    def test_indentation_with_replacing_spaces_with_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with spaces with tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '        foo',
                '\tfoo'),
            None)

    def test_indentation_with_no_changes(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        without changes
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '    foo'),
            None)

    def test_unindentation_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '        foo',
                '    foo'),
            (False, 4, 4))

    def test_unindentation_with_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\t    foo',
                '    foo'),
            (False, 1, 8))

    def test_unindentation_with_spaces_and_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting spaces and tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '  \t    foo',
                '    foo'),
            (False, 3, 8))

    def test_unindentation_with_tabs_and_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting tabs and spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\t      foo',
                '    foo'),
            (False, 3, 10))

    def test_unindentation_with_replacing_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with replacing tabs with spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\tfoo',
                '    foo'),
            (False, 1, 4))

    def test_unindentation_with_replacing_some_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with replacing some tabs with spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\t\t\tfoo',
                '\t        foo'),
            (False, 3, 8))
            'newfile': True,
            'interfilediff': None,
            'filediff': FileDiff(),


class DiffUtilsTests(TestCase):
    """Unit tests for diffutils."""
    def test_get_line_changed_regions(self):
        """Testing DiffChunkGenerator._get_line_changed_regions"""
        def deep_equal(A, B):
            typea, typeb = type(A), type(B)
            self.assertEqual(typea, typeb)

            if typea is tuple or typea is list:
                for a, b in zip_longest(A, B):
                    deep_equal(a, b)
            else:
                self.assertEqual(A, B)

        deep_equal(diffutils.get_line_changed_regions(None, None),
                   (None, None))

        old = 'submitter = models.ForeignKey(Person, verbose_name="Submitter")'
        new = 'submitter = models.ForeignKey(User, verbose_name="Submitter")'
        regions = diffutils.get_line_changed_regions(old, new)
        deep_equal(regions, ([(30, 36)], [(30, 34)]))

        old = '-from reviews.models import ReviewRequest, Person, Group'
        new = '+from .reviews.models import ReviewRequest, Group'
        regions = diffutils.get_line_changed_regions(old, new)
        deep_equal(regions, ([(0, 1), (6, 6), (43, 51)],
                             [(0, 1), (6, 7), (44, 44)]))

        old = 'abcdefghijklm'
        new = 'nopqrstuvwxyz'
        regions = diffutils.get_line_changed_regions(old, new)
        deep_equal(regions, (None, None))