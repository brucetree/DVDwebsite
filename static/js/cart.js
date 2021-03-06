let updateBtns = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        // console.log('productId', productId, 'action', action);

        // console.log('USER: ', user);
        if (user == 'AnonymousUser') {
            console.log('User is not authenticated');
            alert("Sorry, please log in firstly");
        } else {
            // console.log('User is authenticated, sending data...');
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...');
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (action=='add'){
                 alert("add  successful");
            }
            else if (action=='remove'){
                alert("remove successful");
            }
            else{
                 alert("delete successful");
            }
            location.reload();
            // console.log('Data:', data)
        });
}