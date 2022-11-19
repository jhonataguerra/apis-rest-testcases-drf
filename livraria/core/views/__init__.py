# Testar e demonstrar as diferentes formas de criar e customizar Views
from .testesIniciais import teste
from .categoriaClass import CategoriaView
from .categoriaApiView import CategoriasDetail, CategoriasList
from .categoriaGenericView import CategoriaDetailGeneric, CategoriasListGeneric

# Modo a ser usado no restante do projeto
from .categoria import CategoriaViewSet
from .editora import EditoraViewSet
