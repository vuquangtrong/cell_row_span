from markdown.test_tools import TestCase
from cell_row_span import CellRowSpanExtension


class rowspan(TestCase):
    def runTest(self):
        src = self.dedent("""
        c11 | c12 | c13
        ----|-----|-----
        c21 | c22 | c23
        c31 |_   _| c32
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
        <td>c21</td>
        <td rowspan="2">c22</td>
        <td>c23</td>
        </tr>
        <tr>
        <td>c31</td>
        <td>c32</td>
        </tr>
        </tbody>
        </table>
        """)
        self.assertMarkdownRenders(src, exp, output_format="html",
                                   extensions=['tables',
                                               CellRowSpanExtension()])
