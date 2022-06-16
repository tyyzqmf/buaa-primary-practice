# 方向检测
DIRECTION = {
    -1: "未定义",
    0: "正向",
    1: "逆时针90度",
    2: "逆时针180度",
    3: "逆时针270度"
}

# 身份证状态
IMAGESTATUS = {
    "normal": "识别正常",
    "reversed_side": "身份证正反面颠倒",
    "non_idcard": "上传的图片中不包含身份证",
    "blurred": "身份证模糊",
    "other_type_card": "其他类型证照",
    "over_exposure": "身份证关键字段反光或过曝",
    "over_dark": "身份证欠曝（亮度过低）",
    "unknown": "未知状态"
}

# 银行卡类型
BANKCARDTYPE = {
    0: "不能识别",
    1: "借记卡",
    2: "贷记卡（原信用卡大部分为贷记卡）",
    3: "准贷记卡",
    4: "预付费卡"
}
