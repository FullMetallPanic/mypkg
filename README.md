# Texas Hold’em ポーカー

[![test](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml)

---

## ノードの説明


### dealer
- 役割: ディーラーとして手札とテーブルカードを生成して配信
- ノード名: `poker_dealer`
- パブリッシュトピック: `/poker_table`
- 更新間隔: 0.5 秒

### judge
- 役割: 配牌を受信し、ポーカー役判定を行い `/poker_result` に配信
- ノード名: `poker_judge`
- サブスクライブトピック: `/poker_table`
- パブリッシュトピック: `/poker_result`

### listener
- 役割: `/poker_table` と `/poker_result` の情報を受信してコンソールに表示
- ノード名: `poker_listener`
- サブスクライブするトピック: `/poker_table`, `/poker_result`

---

## トピックの仕様

| トピック名       | 型                     | 内容                                     |
|------------------|------------------------|----------------------------------------|
| `/poker_table`    | `std_msgs/String`      | 手札とテーブルカードをJSON 形式で配信 |
| `/poker_result`   | `std_msgs/String`      | 判定結果をJSON 形式で配信             |

---

## 実行方法
ディーラー＋ジャッジをまとめて実行
```
$ ros2 launch mypkg talk_listen.launch.py
[dealer-1] [INFO] [1767760898.296583183] [poker_dealer]: Poker Dealer Started
[dealer-1] [INFO] [1767760898.297576598] [poker_dealer]: Deal: {"hole": ["3C", "TD"], "community": ["7D", "KD", "2D", "5D", "8H"]}
[listener-3] [INFO] [1767760898.299860827] [poker_listener]: Poker Listener Started
[listener-3] [INFO] [1767760898.301207145] [poker_listener]:
[listener-3] === Texas Hold'em Result ===
[listener-3] Hole Cards   : 3C TD
[listener-3] Community    : 7D KD 2D 5D 8H
[listener-3] Best Hand    : Flush
```

個別ノード実行
- 別端末で起動して確認
```
$ ros2 run mypkg dealer
[INFO] [1767761091.692478039] [poker_dealer]: Poker Dealer Started
[INFO] [1767761091.693720691] [poker_dealer]: Deal: {"hole": ["8S", "2C"], "community": ["JS", "TH", "9H", "KD", "QS"]}
```
```
$ ros2 run mypkg judge
[INFO] [1767761026.910593741] [poker_judge]: Poker Judge Started
[INFO] [1767761091.695931376] [poker_judge]: Judged: {"hole": ["8S", "2C"], "community": ["JS", "TH", "9H", "KD", "QS"], "result": "Straight"}
```
```
$ ros2 run mypkg listener
[INFO] [1767761085.010743675] [poker_listener]: Poker Listener Started
[INFO] [1767761091.694904665] [poker_listener]:
=== Texas Hold'em Result ===
Hole Cards   : 8S 2C
Community    : JS TH 9H KD QS
Best Hand    : Straight
```


## テスト環境
- Ubuntu 22.04 LTS
- Python 3.10.12
- ROS 2 Humble Hawksbill


## 謝辞
- [ポーカーにおける役の一覧・手札強弱](https://ja.wikipedia.org/wiki/ポーカー・ハンドの一覧)

- [Poker 手札評価アルゴリズムの一例：Effective Hand Strength](https://en.wikipedia.org/wiki/Effective_hand_strength_algorithm)

- [Python Algorithm to Determine Winner in Texas Hold’em](https://stackoverflow.com/questions/5293405/algorithm-to-determine-the-winner-of-a-texas-holdem-hand)

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- @ 2025 Hayato Matsumoto
