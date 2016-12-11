$(function () {
        $('#submitButtonCreateNewExhibit').click(function () {
            $.ajax({
                url: '/addExhibit',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(JSON.stringify(error));
                }
            });
        });
    }),
    $(function () {
        $('#submitButtonCreateNewPiece').click(function () {
            $.ajax({
                url: '/addPiece',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(error)
                        // console.log(JSON.stringify(error));
                }
            });
        });
    }),
    $(function () {
        $('#submitButtonAddNewCurator').click(function () {
            $.ajax({
                url: '/addCurator',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(JSON.stringify(error));
                }
            });
        });
    }),
    $(function () {
        $('#submitButtonAddNewDonor').click(function () {
            $.ajax({
                url: '/addDonor',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(JSON.stringify(error));
                }
            });
        });
    }),
    $(function () {
        $('#submitButtonLogNewDonation').click(function () {
            $.ajax({
                url: '/logDonation',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(JSON.stringify(error));
                }
            });
        });
    }),
    $(function () {
        $('#submitButtonAddPieceToExhibit').click(function () {
            $.ajax({
                url: '/addPieceToExhibit',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(JSON.stringify(error));
                }
            });
        });
    });