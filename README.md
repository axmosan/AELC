# AELanguageChanger
Adobe After Effectsで簡単に言語設定を日本語から英語に変更することが出来るGUIソフトウェアです。

![AELC_Preview](https://github.com/user-attachments/assets/7f7caa56-4e21-43e0-a94d-c58cfc2b350d)

## 仕様

After Effectsはドキュメント直下に【ae_force_english.txt】というテキストファイルがあれば強制的に言語が英語の状態で起動されます。

![image](https://github.com/user-attachments/assets/dc4bbbfc-207d-4a1a-a5ca-74a1505b1158)

このソフトウェアでは、起動して
【Japanese】を選択すると【ae_force_english.txt】がある場合はそれを削除し、【ae_force_japanese.txt】を作成して日本語起動状態にします。
【English】を選択すると【ae_force_japanese.txt】がある場合はそれを削除し、【ae_force_english.txt】を作成して英語起動状態にします。

頻繁にAeの言語を変更するニッチな使い方をする方向けのソフトウェアです。

初回起動時にWindows Defenderが反応してしまうのは仕様です。
