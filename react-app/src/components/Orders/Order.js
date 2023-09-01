import Review from "../Reviews/Review";
import OpenModalButton from "../OpenModalButton";
import CreateReview from "../Reviews/CreateReview/CreateReview";

const Order = ({ order, reviews }) => {
    const product = order.product;


    const review = (Object.values(reviews).filter(review => review?.id === order.reviewId))[0]
    
    return (
        <div className="orderItem">
            <div>
                <img id="orderImage" className="productTileImage" alt={product.name} src={product.images[0].imageUrl} />
            </div>
            <div className="orderDetails">
                <h3>{product.name}</h3>
                <div>Ordered on: {order.createdAt}</div>
                {review ?
                <div className="orderReview">Your review:
                    <Review review={review} />
                    <div className="editDeleteDiv">
                        <div>
                            <OpenModalButton 
                                // modalComponent={}
                                buttonText={<div className="editButton">Edit</div>}
                            />
                        </div>
                        <div>
                            <OpenModalButton 
                                buttonText={<div className="deleteButton">Delete</div>}
                            />
                        </div>

                    </div>
                </div>
                :
                <OpenModalButton 
                    modalComponent={<CreateReview orderId={order.id} />}
                    buttonText={<div className="createButton">Leave a review</div>}
                />

                }
            </div>
        </div>
    )
}
export default Order;