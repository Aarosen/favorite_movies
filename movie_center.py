import fresh_tomatoes
import movies
 
argo = movies.Movie("Argo", "The true story of how survivors of the US embassy"
                    " in Iran back in 1979 escaped death.",
                    "https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",
                    "https://www.youtube.com/watch?v=w918Eh3fij0")
doctor_strange = movies.Movie("Doctor Strange","The story of how a doctor became"
                              " a superhero",
                              "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                              "https://www.youtube.com/watch?v=HSzx-zryEgM")
dirty_grandpa = movies.Movie("Dirty Grandpa","The story of how an old man does"
                             " things that are not typical for an old man.",
                             "https://upload.wikimedia.org/wikipedia/en/6/62/Dirty_Grandpa_teaser_poster.jpg",
                             "https://www.youtube.com/watch?v=vOAn83vOZLk")
shawshank_redemption = movies.Movie("The Shawshank Redemption","It's the story"
                                    " of a person who is not guilty and was"
                                    " put in jail for no reason, and how he gets out of jail.",
                                    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                    "https://www.youtube.com/watch?v=NmzuHjWmXOc")
awakenings = movies.Movie("Awakenings","The story of a man who has an uncurable
                          " disease and how a doctor tries to make his life"
                          " better.",
                          "https://upload.wikimedia.org/wikipedia/en/2/2b/Awakenings.jpg",
                          "https://www.youtube.com/watch?v=JAz-prw_W2A")
good_will_hunting = movies.Movie("Good Will Hunting","The story of a criminal"
                                 " and how he is discovered by a teacher amazed"
                                 " of his knowledge.",
                                 "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                 "https://www.youtube.com/watch?v=nH9LZOXBMUE")

movies = [argo, doctor_strange, dirty_grandpa, shawshank_redemption, awakenings, good_will_hunting]
fresh_tomatoes.open_movies_page(movies)

