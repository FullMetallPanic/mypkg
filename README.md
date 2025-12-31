# Texas Hold’em ポーカー

[![test](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml)

Texas Hold’em ポーカーの配牌／判定を行う ROS2 パッケージです。  
ROS2 ノードとして以下の機能を提供します：

- `/poker_table`：ディーラーが配ったカード情報を公開
- `/poker_result`：ジャッジが役判定結果を公開


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

## Python モジュールの説明

### dealer.py
- ディーラー処理とトピック配信

### judge.py 
- 役判定処理とトピック配信

### listener.py
- トピック受信して表示

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
```

個別ノード実行
- 別端末で起動
```
$ ros2 run mypkg dealer
$ ros2 run mypkg judge
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
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
@ 2025 Hayato Matsumoto
