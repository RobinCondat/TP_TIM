import time
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize

def chronometrer(fonction,fonction_name,image, *args_fonction):
    t_before = time.time()
    new_image = fonction(image, *args_fonction)
    t_after = time.time()
    print("Temps d'exécution de {0} : {1:.2f} sec".format(fonction_name,t_after-t_before))
    return new_image

def afficher(image,palette,titre=""):
    plt.imshow(image,palette,norm=Normalize(vmin=0, vmax=255, clip=False))
    plt.title(titre)
    plt.show()