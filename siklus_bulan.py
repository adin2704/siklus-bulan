class Node:
    def __init__(self, fase):
        self.fase = fase
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, fase):
        node = Node(fase)

        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = node
            node.next = self.head

    def tampilkan(self):
        if self.head is None:
            print("Data fase bulan kosong")
            return

        current = self.head
        while True:
            print(current.fase)
            current = current.next

            if current == self.head:
                break


bulan = CircularLinkedList()

fase_bulan = [
    "Bulan Baru",
    "Sabit Muda",
    "Perbani Awal",
    "Cembung Awal",
    "Purnama",
    "Cembung Akhir",
    "Perbani Akhir",
    "Sabit Tua"
]

for fase in fase_bulan:
    bulan.tambah(fase)

print("=== SIKLUS FASE BULAN ===")
bulan.tampilkan()