import matplotlib.pyplot as plt

random = {
    "10k": {
        "bubble": 3.876751875,
        "heap": 0.028514374999999995,
        "insertion": 1.759440541,
        "merge": 0.018940665999999995
    },
    "50k": {
        "bubble": 98.22798145799999,
        "heap": 0.1795817909999995,
        "insertion": 44.740931708,
        "merge": 0.11242491700000024
    },
    "100k": {
        "bubble": 394.38566612500006,
        "heap": 0.38935495800001263,
        "insertion": 176.378654791,
        "merge": 0.23895425000000614
    },
}
descending = {
    "10k": {
        "bubble": 6.886257792000038,
        "heap": 0.02857391700001699,
        "insertion": 3.942171333000033,
        "merge": 0.01626854199992067
    },
    "50k": {
        "bubble": 133.42529962499998,
        "heap": 0.17160554199995204,
        "insertion": 89.22219058399992,
        "merge": 0.09176204199991389
    },
    "100k": {
        "bubble": 535.7625365420001,
        "heap": 0.36146770799996375,
        "insertion": 354.96300070899997,
        "merge": 0.19271595800000796
    },
}
ascending = {
    "10k": {
        "bubble": 0.0004565409999486292,
        "heap": 0.030809583000063867,
        "insertion": 0.0008521669999481674,
        "merge": 0.015432584000109273
    },
    "50k": {
        "bubble": 0.002349333999973169,
        "heap": 0.18525533399997585,
        "insertion": 0.004289707999987513,
        "merge": 0.08835374999989654
    },
    "100k": {
        "bubble": 0.004659749999973428,
        "heap": 0.3959647500000756,
        "insertion": 0.008595458000172584,
        "merge": 0.18697416700001668
    }
}


def get_plot_quantity(title, bubble, heap, insertion, merge):
    order = ['Embaralhado', 'Inversamente ordenado', 'Ordenado']

    fig, axs = plt.subplots()

    axs.plot(order, bubble, label='Bubble', color='purple')
    axs.plot(order, heap, label='Heap', color='red')
    axs.plot(order, insertion, label='Insertion', color='blue', linestyle='--')
    axs.plot(order, merge, label='Merge', color='green', linestyle='--')

    axs.legend()

    plt.xlabel('Ordenação')
    plt.ylabel('Tempo (s)')
    plt.title(title)
    plt.grid(True)

    plt.show()


def get_plot_quantity_2(title, bubble, heap, insertion, merge):
    order = ['Ordenado', 'Embaralhado', 'Inversamente ordenado']
    fig, axs = plt.subplots()

    axs.plot(order, bubble, label='Bubble', color='purple')
    axs.plot(order, heap, label='Heap', color='red')
    axs.plot(order, insertion, label='Insertion', color='blue', linestyle='--')
    axs.plot(order, merge, label='Merge', color='green', linestyle='--')

    axs.legend()

    plt.xlabel('Ordenação')
    plt.ylabel('Tempo (s)')
    plt.title(title)
    plt.grid(True)

    plt.show()


def get_plot_order(title, bubble, heap, insertion, merge):
    quantity = ['10k', '50k', '100k']
    fig, axs = plt.subplots()

    axs.plot(quantity, bubble, label='Bubble', color='purple')
    axs.plot(quantity, heap, label='Heap', color='red')
    axs.plot(quantity, insertion, label='Insertion', color='blue', linestyle='--')
    axs.plot(quantity, merge, label='Merge', color='green', linestyle='--')

    axs.legend()

    plt.xlabel('Quantidade')
    plt.ylabel('Tempo (s)')
    plt.title(title)
    plt.grid(True)

    plt.show()


# Por quantidade

bubble_10k = [random["10k"]["bubble"], descending["10k"]["bubble"], ascending["10k"]["bubble"]]
heap_10k = [random["10k"]["heap"], descending["10k"]["heap"], ascending["10k"]["heap"]]
insertion_10k = [random["10k"]["insertion"], descending["10k"]["insertion"], ascending["10k"]["insertion"]]
merge_10k = [random["10k"]["merge"], descending["10k"]["merge"], ascending["10k"]["merge"]]

get_plot_quantity('Comparação com 10.000 items', bubble_10k, heap_10k, insertion_10k, merge_10k)

bubble_50k = [random["50k"]["bubble"], descending["50k"]["bubble"], ascending["50k"]["bubble"]]
heap_50k = [random["50k"]["heap"], descending["50k"]["heap"], ascending["50k"]["heap"]]
insertion_50k = [random["50k"]["insertion"], descending["50k"]["insertion"], ascending["50k"]["insertion"]]
merge_50k = [random["50k"]["merge"], descending["50k"]["merge"], ascending["50k"]["merge"]]

get_plot_quantity('Comparação com 50.000 items', bubble_50k, heap_50k, insertion_50k, merge_50k)

bubble_100k = [random["100k"]["bubble"], descending["100k"]["bubble"], ascending["100k"]["bubble"]]
heap_100k = [random["100k"]["heap"], descending["100k"]["heap"], ascending["100k"]["heap"]]
insertion_100k = [random["100k"]["insertion"], descending["100k"]["insertion"], ascending["100k"]["insertion"]]
merge_100k = [random["100k"]["merge"], descending["100k"]["merge"], ascending["100k"]["merge"]]

get_plot_quantity('Comparação com 100.000 items', bubble_100k, heap_100k, insertion_100k, merge_100k)

# Por quantidade 2

bubble_10k = [ascending["10k"]["bubble"], random["10k"]["bubble"], descending["10k"]["bubble"]]
heap_10k = [ascending["10k"]["heap"], random["10k"]["heap"], descending["10k"]["heap"]]
insertion_10k = [ascending["10k"]["insertion"], random["10k"]["insertion"], descending["10k"]["insertion"]]
merge_10k = [ascending["10k"]["merge"], random["10k"]["merge"], descending["10k"]["merge"]]

get_plot_quantity_2('Comparação com 10.000 items', bubble_10k, heap_10k, insertion_10k, merge_10k)

bubble_50k = [ascending["50k"]["bubble"], random["50k"]["bubble"], descending["50k"]["bubble"]]
heap_50k = [ascending["50k"]["heap"], random["50k"]["heap"], descending["50k"]["heap"]]
insertion_50k = [ascending["50k"]["insertion"], random["50k"]["insertion"], descending["50k"]["insertion"]]
merge_50k = [ascending["50k"]["merge"], random["50k"]["merge"], descending["50k"]["merge"]]

get_plot_quantity_2('Comparação com 50.000 items', bubble_50k, heap_50k, insertion_50k, merge_50k)

bubble_100k = [ascending["100k"]["bubble"], random["100k"]["bubble"], descending["100k"]["bubble"]]
heap_100k = [ascending["100k"]["heap"], random["100k"]["heap"], descending["100k"]["heap"]]
insertion_100k = [ascending["100k"]["insertion"], random["100k"]["insertion"], descending["100k"]["insertion"]]
merge_100k = [ascending["100k"]["merge"], random["100k"]["merge"], descending["100k"]["merge"]]

get_plot_quantity_2('Comparação com 100.000 items', bubble_100k, heap_100k, insertion_100k, merge_100k)

# Por ordenação

bubble_ascending = [ascending["10k"]["bubble"], ascending["50k"]["bubble"], ascending["100k"]["bubble"]]
heap_ascending = [ascending["10k"]["heap"], ascending["50k"]["heap"], ascending["100k"]["heap"]]
insertion_ascending = [ascending["10k"]["insertion"], ascending["50k"]["insertion"], ascending["100k"]["insertion"]]
merge_ascending = [ascending["10k"]["merge"], ascending["50k"]["merge"], ascending["100k"]["merge"]]

get_plot_order('Comparação com items já ordenados', bubble_ascending, heap_ascending, insertion_ascending, merge_ascending)

bubble_descending = [descending["10k"]["bubble"], descending["50k"]["bubble"], descending["100k"]["bubble"]]
heap_descending = [descending["10k"]["heap"], descending["50k"]["heap"], descending["100k"]["heap"]]
insertion_descending = [descending["10k"]["insertion"], descending["50k"]["insertion"], descending["100k"]["insertion"]]
merge_descending = [descending["10k"]["merge"], descending["50k"]["merge"], descending["100k"]["merge"]]

get_plot_order('Comparação com items inversamente ordenados', bubble_descending, heap_descending, insertion_descending, merge_descending)

bubble_random = [random["10k"]["bubble"], random["50k"]["bubble"], random["100k"]["bubble"]]
heap_random = [random["10k"]["heap"], random["50k"]["heap"], random["100k"]["heap"]]
insertion_random = [random["10k"]["insertion"], random["50k"]["insertion"], random["100k"]["insertion"]]
merge_random = [random["10k"]["merge"], random["50k"]["merge"], random["100k"]["merge"]]

get_plot_order('Comparação com items embaralhados', bubble_random, heap_random, insertion_random, merge_random)
