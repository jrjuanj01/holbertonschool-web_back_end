export default class Car {
  /**
     *
     * @param {String} brand
     * @param {String} motor
     * @param {String} color
     */
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const NewObj = this.constructor[Symbol.species] || this.constructor;
    const Clone = new NewObj();
    return new Clone();
  }
}
