from absl import flags

# 定義所有標誌
flags.DEFINE_string("video", "./data/test3.mp4", "輸入視頻路徑或攝像頭索引（例如 0）")
flags.DEFINE_string("output", "./output/input.mp4", "輸出視頻路徑")
flags.DEFINE_float("conf", 0.3, "置信度閾值")
flags.DEFINE_integer("class_id", None, "要跟踪的類別ID（例如2代表汽車）")
FLAGS = flags.FLAGS