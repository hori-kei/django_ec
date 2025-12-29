# cart/utils.py
from .models import Cart


def get_or_create_cart(request):
    """
    ブラウザ（セッション）ごとに Cart を取得する。
    セッションキーが無ければ発行し、その session_key で Cart を作成/取得する。
    """
    if request.session.session_key is None:
        request.session.create()

    session_key = request.session.session_key
    cart, _created = Cart.objects.get_or_create(session_key=session_key)
    return cart
