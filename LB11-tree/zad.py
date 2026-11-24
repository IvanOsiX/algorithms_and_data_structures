class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    # Если дерево пустое, создаем корневой узел
    if root is None:
        return Node(value)
    
    # Если значение меньше корня, идем влево
    if value < root.value:
        root.left = insert(root.left, value)
    # Иначе идем вправо
    else:
        root.right = insert(root.right, value)
    return root

# Функция обхода дерева

def inorder_traversal(root):
    """Симметричный обход: Лево -> Корень -> Право (выводит по возрастанию)"""
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Основная программа
print("Создаем бинарное дерево поиска.")
tree = None

while True:
    try:
        print("\nВведите целое число для добавления в дерево (или 'q' для завершения):")
        user_input = input()
        
        if user_input.lower() == 'q':
            break
            
        value = int(user_input)
        tree = insert(tree, value)
        print(f"Число {value} добавлено.")
        
    except ValueError:
        print("Ошибка! Введите целое число или 'q'.")

# Проверка, что дерево не пустое, прежде чем делать обход
if tree is not None:
    print("\n--- Результаты обхода дерева ---")
    
    print("Симметричный обход (In-order):")
    inorder_traversal(tree)
    print()

else:
    print("\nДерево пустое, обходить нечего.")