# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = lunar_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class PreviewImage:
    aspect_ratio: float
    height: int
    width: int
    src: str

    @staticmethod
    def from_dict(obj: Any) -> 'PreviewImage':
        assert isinstance(obj, dict)
        aspect_ratio = from_float(obj.get("aspect_ratio"))
        height = from_int(obj.get("height"))
        width = from_int(obj.get("width"))
        src = from_str(obj.get("src"))
        return PreviewImage(aspect_ratio, height, width, src)

    def to_dict(self) -> dict:
        result: dict = {}
        result["aspect_ratio"] = to_float(self.aspect_ratio)
        result["height"] = from_int(self.height)
        result["width"] = from_int(self.width)
        result["src"] = from_str(self.src)
        return result


@dataclass
class Media:
    alt: None
    id: int
    position: int
    preview_image: PreviewImage
    aspect_ratio: float
    height: int
    media_type: str
    src: str
    width: int

    @staticmethod
    def from_dict(obj: Any) -> 'Media':
        assert isinstance(obj, dict)
        alt = from_none(obj.get("alt"))
        id = from_int(obj.get("id"))
        position = from_int(obj.get("position"))
        preview_image = PreviewImage.from_dict(obj.get("preview_image"))
        aspect_ratio = from_float(obj.get("aspect_ratio"))
        height = from_int(obj.get("height"))
        media_type = from_str(obj.get("media_type"))
        src = from_str(obj.get("src"))
        width = from_int(obj.get("width"))
        return Media(alt, id, position, preview_image, aspect_ratio, height, media_type, src, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["alt"] = from_none(self.alt)
        result["id"] = from_int(self.id)
        result["position"] = from_int(self.position)
        result["preview_image"] = to_class(PreviewImage, self.preview_image)
        result["aspect_ratio"] = to_float(self.aspect_ratio)
        result["height"] = from_int(self.height)
        result["media_type"] = from_str(self.media_type)
        result["src"] = from_str(self.src)
        result["width"] = from_int(self.width)
        return result


@dataclass
class Option:
    name: str
    position: int
    values: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        position = from_int(obj.get("position"))
        values = from_list(from_str, obj.get("values"))
        return Option(name, position, values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["position"] = from_int(self.position)
        result["values"] = from_list(from_str, self.values)
        return result


@dataclass
class FeaturedImage:
    id: int
    product_id: int
    position: int
    created_at: datetime
    updated_at: datetime
    alt: None
    width: int
    height: int
    src: str
    variant_ids: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'FeaturedImage':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        product_id = from_int(obj.get("product_id"))
        position = from_int(obj.get("position"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        alt = from_none(obj.get("alt"))
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        src = from_str(obj.get("src"))
        variant_ids = from_list(from_int, obj.get("variant_ids"))
        return FeaturedImage(id, product_id, position, created_at, updated_at, alt, width, height, src, variant_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["product_id"] = from_int(self.product_id)
        result["position"] = from_int(self.position)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["alt"] = from_none(self.alt)
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["src"] = from_str(self.src)
        result["variant_ids"] = from_list(from_int, self.variant_ids)
        return result


@dataclass
class FeaturedMedia:
    alt: None
    id: int
    position: int
    preview_image: PreviewImage

    @staticmethod
    def from_dict(obj: Any) -> 'FeaturedMedia':
        assert isinstance(obj, dict)
        alt = from_none(obj.get("alt"))
        id = from_int(obj.get("id"))
        position = from_int(obj.get("position"))
        preview_image = PreviewImage.from_dict(obj.get("preview_image"))
        return FeaturedMedia(alt, id, position, preview_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["alt"] = from_none(self.alt)
        result["id"] = from_int(self.id)
        result["position"] = from_int(self.position)
        result["preview_image"] = to_class(PreviewImage, self.preview_image)
        return result


@dataclass
class Variant:
    id: int
    title: str
    option1: str
    option2: None
    option3: None
    sku: str
    requires_shipping: bool
    taxable: bool
    featured_image: FeaturedImage
    available: bool
    name: str
    public_title: str
    options: List[str]
    price: int
    weight: int
    compare_at_price: None
    inventory_management: str
    barcode: str
    featured_media: FeaturedMedia
    requires_selling_plan: bool
    selling_plan_allocations: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        option1 = from_str(obj.get("option1"))
        option2 = from_none(obj.get("option2"))
        option3 = from_none(obj.get("option3"))
        sku = from_str(obj.get("sku"))
        requires_shipping = from_bool(obj.get("requires_shipping"))
        taxable = from_bool(obj.get("taxable"))
        featured_image = FeaturedImage.from_dict(obj.get("featured_image"))
        available = from_bool(obj.get("available"))
        name = from_str(obj.get("name"))
        public_title = from_str(obj.get("public_title"))
        options = from_list(from_str, obj.get("options"))
        price = from_int(obj.get("price"))
        weight = from_int(obj.get("weight"))
        compare_at_price = from_none(obj.get("compare_at_price"))
        inventory_management = from_str(obj.get("inventory_management"))
        barcode = from_str(obj.get("barcode"))
        featured_media = FeaturedMedia.from_dict(obj.get("featured_media"))
        requires_selling_plan = from_bool(obj.get("requires_selling_plan"))
        selling_plan_allocations = from_list(lambda x: x, obj.get("selling_plan_allocations"))
        return Variant(id, title, option1, option2, option3, sku, requires_shipping, taxable, featured_image, available, name, public_title, options, price, weight, compare_at_price, inventory_management, barcode, featured_media, requires_selling_plan, selling_plan_allocations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["option1"] = from_str(self.option1)
        result["option2"] = from_none(self.option2)
        result["option3"] = from_none(self.option3)
        result["sku"] = from_str(self.sku)
        result["requires_shipping"] = from_bool(self.requires_shipping)
        result["taxable"] = from_bool(self.taxable)
        result["featured_image"] = to_class(FeaturedImage, self.featured_image)
        result["available"] = from_bool(self.available)
        result["name"] = from_str(self.name)
        result["public_title"] = from_str(self.public_title)
        result["options"] = from_list(from_str, self.options)
        result["price"] = from_int(self.price)
        result["weight"] = from_int(self.weight)
        result["compare_at_price"] = from_none(self.compare_at_price)
        result["inventory_management"] = from_str(self.inventory_management)
        result["barcode"] = from_str(self.barcode)
        result["featured_media"] = to_class(FeaturedMedia, self.featured_media)
        result["requires_selling_plan"] = from_bool(self.requires_selling_plan)
        result["selling_plan_allocations"] = from_list(lambda x: x, self.selling_plan_allocations)
        return result


@dataclass
class Lunar:
    id: int
    title: str
    handle: str
    description: str
    published_at: datetime
    created_at: datetime
    vendor: str
    type: str
    tags: List[Any]
    price: int
    price_min: int
    price_max: int
    available: bool
    price_varies: bool
    compare_at_price: None
    compare_at_price_min: int
    compare_at_price_max: int
    compare_at_price_varies: bool
    variants: List[Variant]
    images: List[str]
    featured_image: str
    options: List[Option]
    url: str
    media: List[Media]
    requires_selling_plan: bool
    selling_plan_groups: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Lunar':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        handle = from_str(obj.get("handle"))
        description = from_str(obj.get("description"))
        published_at = from_datetime(obj.get("published_at"))
        created_at = from_datetime(obj.get("created_at"))
        vendor = from_str(obj.get("vendor"))
        type = from_str(obj.get("type"))
        tags = from_list(lambda x: x, obj.get("tags"))
        price = from_int(obj.get("price"))
        price_min = from_int(obj.get("price_min"))
        price_max = from_int(obj.get("price_max"))
        available = from_bool(obj.get("available"))
        price_varies = from_bool(obj.get("price_varies"))
        compare_at_price = from_none(obj.get("compare_at_price"))
        compare_at_price_min = from_int(obj.get("compare_at_price_min"))
        compare_at_price_max = from_int(obj.get("compare_at_price_max"))
        compare_at_price_varies = from_bool(obj.get("compare_at_price_varies"))
        variants = from_list(Variant.from_dict, obj.get("variants"))
        images = from_list(from_str, obj.get("images"))
        featured_image = from_str(obj.get("featured_image"))
        options = from_list(Option.from_dict, obj.get("options"))
        url = from_str(obj.get("url"))
        media = from_list(Media.from_dict, obj.get("media"))
        requires_selling_plan = from_bool(obj.get("requires_selling_plan"))
        selling_plan_groups = from_list(lambda x: x, obj.get("selling_plan_groups"))
        return Lunar(id, title, handle, description, published_at, created_at, vendor, type, tags, price, price_min, price_max, available, price_varies, compare_at_price, compare_at_price_min, compare_at_price_max, compare_at_price_varies, variants, images, featured_image, options, url, media, requires_selling_plan, selling_plan_groups)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["handle"] = from_str(self.handle)
        result["description"] = from_str(self.description)
        result["published_at"] = self.published_at.isoformat()
        result["created_at"] = self.created_at.isoformat()
        result["vendor"] = from_str(self.vendor)
        result["type"] = from_str(self.type)
        result["tags"] = from_list(lambda x: x, self.tags)
        result["price"] = from_int(self.price)
        result["price_min"] = from_int(self.price_min)
        result["price_max"] = from_int(self.price_max)
        result["available"] = from_bool(self.available)
        result["price_varies"] = from_bool(self.price_varies)
        result["compare_at_price"] = from_none(self.compare_at_price)
        result["compare_at_price_min"] = from_int(self.compare_at_price_min)
        result["compare_at_price_max"] = from_int(self.compare_at_price_max)
        result["compare_at_price_varies"] = from_bool(self.compare_at_price_varies)
        result["variants"] = from_list(lambda x: to_class(Variant, x), self.variants)
        result["images"] = from_list(from_str, self.images)
        result["featured_image"] = from_str(self.featured_image)
        result["options"] = from_list(lambda x: to_class(Option, x), self.options)
        result["url"] = from_str(self.url)
        result["media"] = from_list(lambda x: to_class(Media, x), self.media)
        result["requires_selling_plan"] = from_bool(self.requires_selling_plan)
        result["selling_plan_groups"] = from_list(lambda x: x, self.selling_plan_groups)
        return result


def lunar_from_dict(s: Any) -> Lunar:
    return Lunar.from_dict(s)


def lunar_to_dict(x: Lunar) -> Any:
    return to_class(Lunar, x)
