# Texas Hold’em ポーカー

[![test](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/FullMetallPanic/mypkg/actions/workflows/test.yml)

本パッケージは、ディーラー・判定・表示を
それぞれ独立した ROS 2 ノードとして提供します。

各ノードはトピック通信により疎結合に設計されており、
必要なノードのみを選択して利用することが可能です。

例えば、
- dealer ノードのみを用いてカード配布のシミュレーションを行う
- judge ノードのみを用いて外部から受信したカード情報を評価する

といった使い方ができます。


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

###holdem_judge.py
- 役割: テキサスホールデムの役判定アルゴリズムのみを実装した Python モジュール
- ROS 2 依存性: なし
- 利用方法: dealer や judge ノードから import して使用可能であり、単体テストや他アプリケーションへの再利用が可能

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
- 別端末で起動して確認
```
$ ros2 run mypkg dealer
```
```
$ ros2 run mypkg judge
```
```
ros2 run mypkg listener
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
