# def search(request):
#     city = request.GET.get("city", "Anywhere")
#     city = str.capitalize(city)
#     country = request.GET.get("country", "GH")
#     room_type = int(request.GET.get("room_type", 0))
#     price = int(request.GET.get("price", 0))
#     guests = int(request.GET.get("guests", 0))
#     bedrooms = int(request.GET.get("bedrooms", 0))
#     beds = int(request.GET.get("beds", 0))
#     baths = int(request.GET.get("baths", 0))
#     instant = bool(request.GET.get("instant", False))
#     superhost = bool(request.GET.get("superhost", False))
#     selected_amenities = request.GET.getlist("amenities")
#     selected_facilities = request.GET.getlist("facilities")

#     form = {
#         "city": city,
#         "selected_room_type": room_type,
#         "selected_country": country,
#         "price": price,
#         "guests": guests,
#         "bedrooms": bedrooms,
#         "beds": beds,
#         "baths": baths,
#         "selected_amenities": selected_amenities,
#         "selected_facilities": selected_facilities,
#         "instant": instant,
#         "superhost": superhost,
#     }

#     room_types = models.RoomType.objects.all()
#     amenities = models.Amenity.objects.all()
#     facilities = models.Facility.objects.all()

#     choices = {
#         "countries": countries,
#         "room_types": room_types,
#         "amenities": amenities,
#         "facilities": facilities,
#     }

#     filter_args = {}

#     if city != "Anywhere":
#         filter_args["city__startswith"] = city

#     filter_args["country"] = country

#     if room_type != 0:
#         filter_args["room_type__pk"] = room_type

#     if price != 0:
#         filter_args["price__lte"] = price

#     if guests != 0:
#         filter_args["guests__gte"] = guests

#     if bedrooms != 0:
#         filter_args["bedrooms__gte"] = bedrooms

#     if beds != 0:
#         filter_args["beds__gte"] = beds

#     if baths != 0:
#         filter_args["baths__gte"] = baths

#     if instant is True:
#         filter_args["instant_book"] = True

#     if superhost is True:
#         filter_args["host__superhost"] = True

#     if len(selected_amenities) > 0:
#         for selected_amenity in selected_amenities:
#             filter_args["amenities__pk"] = int(selected_amenity)

#     if len(selected_facilities) > 0:
#         for selected_facility in selected_facilities:
#             filter_args["facilities__pk"] = int(selected_facility)

#     rooms = models.Room.objects.filter(**filter_args)

#     return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms},)


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 15)
#     rooms = paginator.get_page(page)
#     return render(request, "rooms/home.html", context={"page": rooms},)


# <form method="get" action="{% url 'rooms:search' %}">
#   <div>
#   <label for="city">City</label>
#         <input
#         value={{city}}
#           name="city"
#           type="text"
#           placeholder="search city"
#         />
#         </div>

#         <div>
#           <label for="country">Country</label>
#           <select name="country" id="country">
#             {% for country in countries %}
#               <option value="{{country.code}}"
#               {% if country.code == selected_country  %}selected
#               {% endif %}>{{country.name}}</option>
#             {% endfor %}
#           </select>
#         </div>

#         <div>
#           <label for="room_type">Room Type</label>
#           <select name="room_type" id="room_type">
#           <option value="0"
#           {% if selected_room_type == 0 %}
#           {% endif %}>Any Kind</option>
#             {% for room_type in room_types %}
#               <option value="{{room_type.pk}}"
#               {% if selected_room_type == room_type.pk %}selected
#               {% endif %}>{{room_type.name}}</option>
#             {% endfor %}
#           </select>
#         </div>

#         <div>
#           <label for="price">Price</label>
#           <input value="{{price}}" type="number" placeholder="Price" id="price" name="price" />
#         </div>

#         <div>
#           <label for="guests">Guests</label>
#           <input value="{{guests}}" type="number" placeholder="Guests" id="guests" name="guests" />
#         </div>

#         <div>
#           <label for="bedrooms">Bedrooms</label>
#           <input value="{{bedrooms}}" type="number" placeholder="Bedrooms" id="bedrooms" name="bedrooms" />
#         </div>

#         <div>
#           <label for="beds">Beds</label>
#           <input value="{{beds}}" type="number" placeholder="Beds" id="beds" name="beds" />
#         </div>

#         <div>
#           <label for="baths">Baths</label>
#           <input value="{{baths}}" type="number" placeholder="Baths" id="baths" name="baths" />
#         </div>

#         <div>
#           <label for="instant">Instant Book Only?</label>
#           <input
#             {% if instant %}
#             checked
#             {% endif %}
#             type="checkbox"
#             id="instant"
#             name="instant" />
#         </div>

#         <div>
#           <label for="superhost">By superhost only?</label>
#           <input
#             {% if superhost %}
#             checked
#             {% endif %}
#             type="checkbox"
#             id="superhost"
#             name="superhost" />
#         </div>

#         <div>
#           <h3>Amenities</h3>
#           <ul>
#             {% for amenity in amenities %}
#               <li>
#                 <label for="a_{{amenity.pk}}">{{amenity.name}}</label>
#                 <input
#                 type="checkbox"
#                 name="amenities"
#                 id="a_{{amenity.pk}}"
#                 value={{amenity.pk}}
#                 {% if amenity.pk|slugify in selected_amenities %}
#                 checked
#                 {% endif %} />
#               </li>
#             {% endfor %}
#           </ul>
#         </div>

#         <div>
#           <h3>Facilities</h3>
#           <ul>
#             {% for facility in facilities %}
#               <li>
#                 <label for="f_{{facility.pk}}">{{facility.name}}</label>
#                 <input
#                 type="checkbox"
#                 name="facilities"
#                 id="f_{{facility.pk}}"
#                 value={{facility.pk}}
#                 {% if facility.pk|slugify in selected_facilities %}
#                 checked
#                 {% endif %} />
#               </li>
#             {% endfor %}
#           </ul>
#         </div>

#         <button type="submit">Search</button>
#       </form>
