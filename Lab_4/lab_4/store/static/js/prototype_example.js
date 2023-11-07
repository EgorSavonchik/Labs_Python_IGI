// Базовый класс "Магазин бытовой химии"
function HouseholdChemistryStore(name, location) {
    this.name = name;
    this.location = location;
    this.inventory = [];
}

HouseholdChemistryStore.prototype.getInventory = function () {
    return this.inventory;
};

HouseholdChemistryStore.prototype.addProduct = function (product) {
    this.inventory.push(product);
};

HouseholdChemistryStore.prototype.findProduct = function (name) {
    return this.inventory.find(product => product.name === name);
};

HouseholdChemistryStore.prototype.sellProduct = function (name) {
    const productIndex = this.inventory.findIndex(product => product.name === name);
    if (productIndex !== -1) {
        const soldProduct = this.inventory.splice(productIndex, 1)[0];
        console.log(`Продан продукт "${name}" из магазина "${this.name}"`);
        return soldProduct;
    } else {
        console.log(`Продукт "${name}" не найден в магазине "${this.name}"`);
    }
};

// Наследник класса "Магазин бытовой химии" с добавлением новых методов
function SpecializedHouseholdChemistryStore(name, location, specialization) {
    HouseholdChemistryStore.call(this, name, location);
    this.specialization = specialization;
}

SpecializedHouseholdChemistryStore.prototype = Object.create(HouseholdChemistryStore.prototype);
SpecializedHouseholdChemistryStore.prototype.constructor = SpecializedHouseholdChemistryStore;

SpecializedHouseholdChemistryStore.prototype.getSpecialization = function () {
    return this.specialization;
};

SpecializedHouseholdChemistryStore.prototype.setSpecialization = function (newSpecialization) {
    this.specialization = newSpecialization;
};

// Декоратор для метода продажи продукта, добавляющий логирование
SpecializedHouseholdChemistryStore.prototype.decorateSellProduct = function (originalSellProduct) {
    return function (name) {
        console.log(`Продажа продукта "${name}" в специализированном магазине "${this.name}"`);
        return originalSellProduct.call(this, name);
    };
};

// Пример использования
const genericStore = new HouseholdChemistryStore("Общий магазин бытовой химии", "Город");
const specializedStore = new SpecializedHouseholdChemistryStore("Детский магазин бытовой химии", "Парк", "Детские товары");

genericStore.addProduct({ name: "Мыло", brand: "Dove" });
specializedStore.addProduct({ name: "Детская зубная паста", brand: "Colgate Kids" });

const decoratedSellProduct = specializedStore.decorateSellProduct(specializedStore.sellProduct);
decoratedSellProduct.call(specializedStore, "Детская зубная паста");

console.log(`Специализация магазина: ${specializedStore.getSpecialization()}`);
specializedStore.setSpecialization("Товары для ванной");
console.log(`Новая специализация магазина: ${specializedStore.getSpecialization()}`);
