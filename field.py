from item import Item
from player import Player
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]]): アイテムのリスト
        blocks (list[Block]): アイテムのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    #  Fieldを生成する関数
    def __init__(
            self,
            players: list[Player],
            enemies: list[Enemy],
            foods: list[Food],
            blocks: list[Block],
            f_size: int = 6) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            foods (list[Food]): アイテムのリスト
            blocks (list[Block]): ブロックのリスト
            f_size (int): フィールドのサイズ
        """
        pass
