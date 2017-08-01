# constraint propagation and search

## initialization
- sudoku 的所有位置填上 '123456789'

## constraint propagation

### eliminate(消除)
- 消除给定位置的给定元素, 比如 eliminate('2357', '3') = '257'
- 若该位置只有 0 个元素, 说明产生了矛盾, 返回 False
- 若该位置只有 1 个元素 d, 则消除该位置所有 peers 中的元素 d
- 对该位置的每个 unit, 遍历 unit 中的每个元素, 统计可以填入 d 的位置
    - 若只有 0 个位置可以填入 d, 则产生矛盾, 返回 False
    - 若只有 1 个位置可以填入 d, 则在该位置填入 d

### assign(填入)
- 对 sudoku 中每个已知的值 d, 将其填入给定位置
- 填入的方式: 循环消除该位置除 d 以外的其他元素

## search
- 从剩余最少(大于1)元素的位置开始搜索, 循环填入该位置可能的值
- 若填入过程中返回 False, 则尝试填入该位置的下一个元素
- 一个位置填好之后, 再继续搜索下一个位置
- 递归搜索, 直到所有位置只剩下一个元素
