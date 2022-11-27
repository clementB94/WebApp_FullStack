// MOVIE
function get_movie(id) {
    return axios.get("/movies/"+id).then(v => v.data)
}

function get_movies(skip, limit) {

}

// RATING

function get_rating(user_id,movie_id){
    return axios.get("/movies/", {
        params: {
          user_id: user_id,
          movie_id:movie_id
        }
      }).then(v => v.data)
}