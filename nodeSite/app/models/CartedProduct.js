/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('CartedProduct', {
    CartedProductID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    ProductID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Product',
        key: 'ProductID'
      }
    },
    CartID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Cart',
        key: 'CartID'
      }
    }
  }, {
    tableName: 'CartedProduct'
  });
};
