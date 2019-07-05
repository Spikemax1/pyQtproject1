self.myTable.setSortingEnabled(True)      сортировка

def selectItems(self):                              весь список выделенных элементов
        elem = self.myTable.currentItem()
        self.myTable.selectRow(elem.row())
        return elem

    def buttonClicked(self):
        elem = self.selectItems().row()
        for i in self.myTable.selectedItems():
            print(i.text())
            
elem = self.selectItems().row()
            self.wind = QtWidgets.QMainWindow()
            self.myTable.selectedItems()
            self.wind.setGeometry(500, 500, 400, 400)

            arrElems = ['Имя', 'Отдел','Подразделение','Телефон','Сотовый']
            arrWidgets = []
            for i in arrElems:
                arrWidgets.append({'name': QtWidgets.QLabel(i, self.wind), 'val': QtWidgets.QLineEdit(i, self.wind)})

            numY = 0
            for elem in range(len(arrWidgets)):
                arrWidgets[elem]['name'].move(elem, numY)
                arrWidgets[elem]['val'].move(elem*50, numY+50)
                numY = elem*50
