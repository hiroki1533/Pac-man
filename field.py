from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    #  Fieldを生成する関数
    def __init__(
            self,
            players: list[Player],
            f_size: int = 6) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            f_size (int): フィールドのサイズ
        """
        
    
        self.f_size = f_size
        self.field = [["　" for _ in range(f_size)] for _ in range(f_size)]
        self.players = players
        # それぞれのアイテムの位置をFieldに反映
        self.update_field()
    

    def update_field(self) -> list[list[str]]:
        """
        敵、プレイヤー、アイテムを配置を参照して、Fieldを更新する関数

        Returns:
            list[list[str]]: 更新されたField

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.update_field()[0]
            ['\\u3000', 'p1', '\\u3000']
            >>> field.update_field()[1]
            ['\\u3000', '\\u3000', '\\u3000']
            >>> field.update_field()[2]
            ['\\u3000', '\\u3000', '\\u3000']
        """
        # fieldを一旦すべて空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = "　"
        #  Fieldを更新する処理を記述
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        return self.field


    def display_field(self) -> None:
        """
        Fieldを表示する関数

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.display_field()
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
             p1
    """
        # 動きか方を表示
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")
        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)  # フィールド内の最大幅を取得

        for row in self.field:
            # 各行の文字列を作成し、不足分を空白文字で埋める
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
