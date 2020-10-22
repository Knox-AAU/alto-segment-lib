from alto_segment_lib.repair_segments import RepairSegments
from alto_segment_lib.segmenter import Segmenter
from alto_segment_lib.segmenter import FindType
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image


if __name__ == '__main__':
    #segmenter = Segmenter("/Users/tlorentzen/Desktop/Example/2006/nordjyskestiftstidende-2006-10-10-01-0829A.alto.xml")
    segmenter = Segmenter("//Users/tlorentzen/Desktop/Example/1942/aalborgstiftstidende-1942-01-02-01-0028B.alto.xml")
    segmenter.set_dpi(300)
    segmenter.set_margin(0)

    #segments_paragraphs = segmenter.find_blocks()
    segments_headers = segmenter.find_segs_with_type(FindType.Header)
    segments_para = segmenter.find_segs_with_type(FindType.Paragraph)

    repair = RepairSegments(segments_para)
    repair.repair_columns()


    #segmenter.font_statistics()
    #segments = segmenter.find_lines()


    #counter = 1

    # Add the patch to the Axes

    #for seg in segments:
    #    plt.gca().add_patch(Rectangle((seg[0], seg[1]), (seg[2]-seg[0]), (seg[3]-seg[1]), linewidth=0.3, edgecolor='r', facecolor='none'))
    #    # plt.text(seg[0]+25, seg[1]+30, "["+str(counter)+"]", horizontalalignment='left', verticalalignment='top')
    #    # plt.text(seg[0]+45, seg[1] + 200, str((seg[2]-seg[0])), horizontalalignment='left', verticalalignment='top')
    #    counter += 1

    # plt.savefig("/Users/tlorentzen/Desktop/Example/1942/aalborgstiftstidende-1942-01-02-01-0028B-out.png", dpi=300, bbox_inches='tight')
