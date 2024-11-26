import time
from player import Player
from field import Field
from user_input import UserInput
from config import Parameters
import logging
import os


logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """ゲームクラスの初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """

        self.player = []
        self.field = None
        self.setup(params)  # ゲームの初期設定


    def setup(self, params: Parameters) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size  # フィールドのサイズ
        # フィールドの初期化
        self.players = [Player(1, 10)]
        self.field = Field(
            self.players,
            f_size)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド．
        キー入力を受け取り，プレイヤーと敵の移動を行い，フィールドを更新する．
        ゲーム終了条件を満たした場合は終了する．

        Returns:
            str: ゲーム終了時のメッセージ (例: "Game Over!", "Game Clear!")
        """
        # ゲームのメインループ
        while True:
            #  フィールドを表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            self.field.display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)
                
                # fieldを更新
            self.field.update_field()

            # 一定の間隔で処理を繰り返す
            # 0.3秒待つ
            time.sleep(0.3)

            # 終了条件のチェック
            # 例えば、全ての食べ物が消えたり、敵とプレイヤーが衝突したりしたら終了する処理を追加する


if __name__ == "__main__":
    main()