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
    return new Car(this._brand, this._motor, this._color);
  }
}
