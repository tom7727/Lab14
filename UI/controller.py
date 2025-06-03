import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._store = None
        self._k = None

    def fillDDStores(self):
        stores = self._model.getAllStores()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(store, on_click = self._choiceStore))


    def handleCreaGrafo(self, e):
        self._store = self._view._ddStore.value
        self._k = self._view._txtIntK.value
        if self._store is None or self._k == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, inserire uno store e un massimo di giorni", color = "red"))
            self._view.update_page()
            return

        try:
            k_int = int(self._k)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append("Attenzione, il numero inserito non è valido")
            self._view.update_page()
            return

        self._model.buildGraph(self._store, k_int)
        nodi, archi = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente!"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {archi}"))
        self._view.update_page()


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass


    def _choiceStore(self, e):
        self._store = self._view._ddStore.value
        print(self._store)