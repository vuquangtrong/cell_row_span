from markdown.test_tools import TestCase
from cell_row_span import CellRowSpanExtension


class colspan(TestCase):
    def runTest(self):
        src = self.dedent("""
        c11 | c12 | c13
        ----|-----|-----
        c21      || c22
        c31 | c32 | c33
        """)
        exp = self.dedent("""
        <table>
        <thead>
        <tr>
        <th>c11</th>
        <th>c12</th>
        <th>c13</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td colspan="2">c21</td>
        <td>c22</td>
        </tr>
        <tr>
        <td>c31</td>
        <td>c32</td>
        <td>c33</td>
        </tr>
        </tbody>
        </table>
        """)
        self.assertMarkdownRenders(src, exp, output_format="html",
                                   extensions=['tables',
                                               CellRowSpanExtension()])
