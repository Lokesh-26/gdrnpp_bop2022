# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague

"""Configuration of the BOP Toolkit."""

import os


######## Basic ########

# Folder with the BOP datasets.
if "BOP_PATH" in os.environ:
    datasets_path = os.environ["BOP_PATH"]
else:
    datasets_path = r"/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/datasets/BOP_DATASETS/"

# Folder with pose results to be evaluated.
#results_path = r'/path/to/folder/with/results'
results_path = r"/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/output/gdrn/br6d/convnext_a6_AugCosyAAEGray_BG05_mlL1_DMask_amodalClipBox_classAware_br6d/inference_model_final/br6d_test"

# Folder for the calculated pose errors and performance scores.
eval_path = r'/path/to/eval/folder'
#eval_path = r"/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/datasets/BOP_DATASETS/"

######## Extended ########

# Folder for outputs (e.g. visualizations).
# output_path = r'/path/to/output/folder'
output_path = r"/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/output/gdrn/br6d"

# For offscreen C++ rendering: Path to the build folder of bop_renderer (github.com/thodan/bop_renderer).
bop_renderer_path = r"/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/bop_renderer/build"

# Executable of the MeshLab server.
# meshlab_server_path = r'/path/to/meshlabserver.exe'
meshlab_server_path = r"/usr/bin/meshlabserver"
