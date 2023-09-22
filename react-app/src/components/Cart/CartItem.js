import { useDispatch, useSelector } from "react-redux"
import { useCart } from "../../context/CartContext";
import './Cart.css'
import { useEffect } from "react";

const CartItem = ({ product }) => {
    const dispatch = useDispatch();
    const { removeFromCart } = useCart();
    if (product == null) return null
    return (
        <li className="cartItem">
            <div className="cartItemContainer">
            <img className="cartImage" alt={product.name} src={product.images[0].imageUrl} />
                <div className="productInfo">
                    
                    <div>{product.name}</div>
                    <div className="productPrice">
                    $ {product.price}
                    </div>
                </div>
                <div>
                    <button className="deleteButtonDesign"
                        onClick={() => removeFromCart(product.id)}
                    >
                        Remove
                    </button>
                </div>
            </div>
            
        </li>
    )
}

export default CartItem;