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
- ノード名: `pokre_dealer`
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


