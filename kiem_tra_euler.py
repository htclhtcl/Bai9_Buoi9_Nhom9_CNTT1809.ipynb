# kiem_tra_euler.py
import networkx as nx
import matplotlib.pyplot as plt

# --- Tạo đồ thị mẫu có chu trình Euler ---
def tao_do_thi_euler_mau():
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    return graph

# --- Tính bậc các đỉnh ---
def tinh_bac_cac_dinh(graph):
    bac_dinh = {}
    for node in graph:
        bac_dinh[node] = len(graph[node])
    return bac_dinh

# --- Kiểm tra liên thông ---
def kiem_tra_lien_thong(graph):
    """
    Kiểm tra liên thông nhưng chỉ xét các đỉnh có bậc > 0.
    Nếu đồ thị không có cạnh (tất cả đỉnh bậc 0) thì xem là liên thông.
    """
    if not graph:
        return True

    # Tập các đỉnh có bậc > 0
    nodes_with_edges = [n for n, neigh in graph.items() if len(neigh) > 0]
    if not nodes_with_edges:
        # không có cạnh -> coi là liên thông (theo ngữ cảnh Euler)
        return True

    start_node = nodes_with_edges[0]
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    # Kiểm tra mọi đỉnh có bậc>0 nằm trong visited
    return all((n in visited) for n in nodes_with_edges)

# --- Kiểm tra Euler ---
def kiem_tra_do_thi_euler(graph):
    """Trả về True nếu đồ thị có chu trình Euler (mọi đỉnh bậc chẵn và liên thông trên đỉnh có cạnh)."""
    if not kiem_tra_lien_thong(graph):
        print("❌ Đồ thị KHÔNG LIÊN THÔNG. - kiem_tra_do_thi_euler.py:56")
        return False
    
    bac_dinh = tinh_bac_cac_dinh(graph)
    for node, bac in bac_dinh.items():
        print(f"Đỉnh {node}: bậc {bac} - kiem_tra_do_thi_euler.py:61")
        if bac % 2 != 0:
            print("❌ Có đỉnh bậc lẻ → KHÔNG phải đồ thị Euler. - kiem_tra_do_thi_euler.py:63")
            return False

    print("✅ Đồ thị liên thông (trên đỉnh có cạnh) và tất cả đỉnh đều bậc chẵn → ĐỒ THỊ EULER. - kiem_tra_do_thi_euler.py:66")
    return True

# --- Vẽ đồ thị ---
def ve_do_thi(graph, title="Đồ thị"):
    """
    Vẽ đồ thị bằng networkx. Đảm bảo thêm cả các đỉnh cô lập (không có cạnh).
    """
    G = nx.Graph()
    # thêm tất cả các đỉnh (kể cả cô lập)
    for n in graph.keys():
        G.add_node(n)
    # thêm cạnh
    for u, neighs in graph.items():
        for v in neighs:
            # để tránh duplicate edges, chỉ thêm khi u<=v (vì graph biểu diễn cả hai chiều)
            if u <= v:
                G.add_edge(u, v)
    # vẽ
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(5,4))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edges(G, pos)
    plt.title(title)
    plt.axis('off')
    plt.show()

# --- Hàm main chạy ví dụ ---
def main():
    print("=== Ví dụ 1: Đồ thị mẫu (hình vuông) === - kiem_tra_do_thi_euler.py:96")
    my_graph = tao_do_thi_euler_mau()
    print("Danh sách kề: - kiem_tra_do_thi_euler.py:98", my_graph)
    ve_do_thi(my_graph, "Đồ thị mẫu (có chu trình Euler)")
    ok = kiem_tra_do_thi_euler(my_graph)
    print("Kết luận: - kiem_tra_do_thi_euler.py:101", "Có chu trình Euler" if ok else "Không có chu trình Euler")
    
    print("\n=== Ví dụ 2: Thêm 1 đỉnh (4) nhưng không nối cạnh === - kiem_tra_do_thi_euler.py:103")
    graph_moi = {n: list(neis) for n, neis in my_graph.items()}
    graph_moi[4] = []  # đỉnh 4 cô lập
    print("Danh sách kề: - kiem_tra_do_thi_euler.py:106", graph_moi)
    ve_do_thi(graph_moi, "Đồ thị thêm đỉnh 4 (cô lập)")
    ok2 = kiem_tra_do_thi_euler(graph_moi)
    print("Kết luận: - kiem_tra_do_thi_euler.py:109", "Có chu trình Euler" if ok2 else "Không có chu trình Euler")
    
    print("\n Gợi ý thử thêm - kiem_tra_do_thi_euler.py:111")
    print("Thử sửa graph_moi để nối đỉnh 4 với một đỉnh (ví dụ graph_moi[4]=[0] và graph_moi[0].append(4)) - kiem_tra_do_thi_euler.py:112")
    print("Rồi chạy lại kiem_tra_do_thi_euler để quan sát kết quả (bậc, liên thông). - kiem_tra_do_thi_euler.py:113")

if __name__ == "__main__":
    main()
