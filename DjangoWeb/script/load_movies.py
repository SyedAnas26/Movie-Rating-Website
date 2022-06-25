from datetime import date


def load_data(apps, schema_editior):
    Movies = apps.get_model("DjangoBackEnd", "MovieRating")
    Movies(MovieTitle='tenet',
           ReleaseDate=date(2020, 12, 11),
           MovieImage='/tenet.jpg',
           UpVotes=42,
           DownVotes=15,
           ).save()

    Movies(MovieTitle='Avengers End Game',
           ReleaseDate=date(2020, 4, 12),
           MovieImage='/avengersEndgame.jpg',
           UpVotes=41,
           DownVotes=2,
           ).save()

    Movies(MovieTitle='Baaghi 3',
           ReleaseDate=date(2020, 6, 11),
           MovieImage='/baaghi3.jpg',
           UpVotes=2,
           DownVotes=90,
           ).save()

    Movies(MovieTitle='Spiderman',
           ReleaseDate=date(2020, 2, 11),
           MovieImage='/spiderman.jpg',
           UpVotes=10,
           DownVotes=2,
           ).save()


    Movies(MovieTitle='Soorarai Potru',
           ReleaseDate=date(2020, 11, 11),
           MovieImage='/sooraraiPotru.jpg',
           UpVotes=3,
           DownVotes=10,
           ).save()


    Movies(MovieTitle='Joker',
           ReleaseDate=date(2020, 5, 11),
           MovieImage='/joker_JAYgzwR.jpg',
           UpVotes=4,
           DownVotes=5,
           ).save()

    Movies(MovieTitle='Kaithi',
           ReleaseDate=date(2019, 10, 12),
           MovieImage='/Karthi_Kaithi.jpg',
           UpVotes=4,
           DownVotes=5,
           ).save()

    Movies(MovieTitle='Vikram',
           ReleaseDate=date(2022, 6, 3),
           MovieImage='/vikram.jpg',
           UpVotes=4,
           DownVotes=5,
           ).save()

    Movies(MovieTitle='KGF CHAPTER 2',
           ReleaseDate=date(2022, 4, 14),
           MovieImage='/kgf2.jpg',
           UpVotes=4,
           DownVotes=5,
           ).save()

    Movies(MovieTitle='Interstellar',
           ReleaseDate=date(2014, 11, 7),
           MovieImage='/interstellar.jpg',
           UpVotes=4,
           DownVotes=5,
           ).save()

