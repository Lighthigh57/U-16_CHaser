# U-16_CHaser
U-16ファイル保存用です。頑張るぞー。
リポジトリは移行しました。
https://github.com/Lighthigh57/U-16CHaser2022

# アクション時のルール
get_ready() → 行動関数 → get_ready() → ... の順で必ず処理を行う。  
行動関数は「内容_方向()」の命名規則に従って名付けられる．

内容は「walk」「look」「search」「put」の4種類．
方向は「right」「up」「left」「down」の4種類．  
この組み合わせで関数を命名．例) walk_up()，search_right() など

行動関数が返すリストは行動後のマップ情報9つ．  
[ ][x][x]  
[ ][C][♡]  
[H][ ][ ]  
このときは [0, 2, 2, 0, 0, 3, 1, 0, 0] が返る．
