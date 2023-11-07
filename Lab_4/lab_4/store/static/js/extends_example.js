// Базовый класс "Магазин бытовой химии"
class ChemistryStore {
    constructor(name, location) {
        this.name = name;
        this.location = location;
        this.inventory = [];
    }

    getInventory() {
        return this.inventory;
    }

    addProduct(product) {
        this.inventory.push(product);
    }

    findProduct(name) {
        return this.inventory.find(product => product.name === name);
    }

    sellProduct(name) {
        const productIndex = this.inventory.findIndex(product => product.name === name);
        if (productIndex !== -1) {
            const soldProduct = this.inventory.splice(productIndex, 1)[0];
            console.log(`Продан продукт "${name}" из магазина "${this.name}"`);
            return soldProduct;
        } else {
            console.log(`Продукт "${name}" не найден в магазине "${this.name}"`);
        }
    }
}

// Наследник класса "Магазин бытовой химии" с добавлением новых методов
class SpecializedChemistryStore extends ChemistryStore {
    constructor(name, location, specialization) {
        super(name, location);
        this.specialization = specialization;
    }

    getSpecialization() {
        return this.specialization;
    }

    setSpecialization(newSpecialization) {
        this.specialization = newSpecialization;
    }

    // Декоратор для метода продажи продукта, добавляющий логирование
    decorateSell(originalSellProduct) {
        return function (name) {
            console.log(`Продажа продукта "${name}" в специализированном магазине "${this.name}"`);
            return originalSellProduct.call(this, name);
        };
    }
}

// Пример использования
const store = new ChemistryStore("Общий магазин бытовой химии", "Город");
const specialStore = new SpecializedChemistryStore("Детский магазин бытовой химии", "Парк", "Детские товары");

store.addProduct({ name: "Мыло", brand: "Dove" });
specialStore.addProduct({ name: "Детская зубная паста", brand: "Colgate Kids" });

const decoratedSell = specialStore.decorateSell(specialStore.sellProduct);
decoratedSell.call(specialStore, "Детская зубная паста");

console.log(`Специализация магазина: ${specialStore.getSpecialization()}`);
specialStore.setSpecialization("Товары для ванной");
console.log(`Новая специализация магазина: ${specialStore.getSpecialization()}`);
