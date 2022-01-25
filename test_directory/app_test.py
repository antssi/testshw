import old_HW
import mock
import builtins

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


class TestOldHw:



    def test_show_all_docs_info_true(self):
        assert ('passport 2207 876234 Василий Гупкин\n' \
                'invoice 11-2 Геннадий Покемонов\n' \
                'insurance 10006 Аристарх Павлов') == old_HW.show_all_docs_info(documents)

    def test_show_all_docs_info_false(self):
        assert ('passport 2207 876234 Василий Пупкин\n' \
                'invoice 11-2 Евгений Покемонов\n' \
                'insurance 10006 Аристарх Павлов') != old_HW.show_all_docs_info(documents)



    def test_check_document_existance_true(self):
        assert old_HW.check_document_existance('11-2') == True

    def test_check_document_existance_false(self):
        assert old_HW.check_document_existance('абц-123?23чя') == False



    def test_add_new_doc_true(self):
        assert ('passport 2207 876234 Василий Гупкин\n' \
                'invoice 11-2 Геннадий Покемонов\n' \
                'insurance 10006 Аристарх Павлов\n' \
                'test 5 test1', \
                {'1': ['2207 876234', '11-2', '5455 028765'], \
                 '2': ['10006'], \
                 '3': [], \
                 '7': ['5']}) == old_HW.add_new_doc('5', 'test', 'test1', '7')

    def test_add_new_doc_false(self):
        assert ('passport 2207 876234 Василий Гупкин\n' \
                'invoice 11-2 Геннадий Покемонов\n' \
                'insurance 10006 Аристарх Павлов\n' \
                'test 5 test1', \
                {'1': ['2207 876234', '11-2', '5455 028765'], \
                 '2': ['10006'], \
                 '3': [], \
                 '7': ['5']}) != old_HW.add_new_doc('1232', 'asdq', 'te123st1', 'ad')



    def test_delete_doc_true(self):
        with mock.patch.object(builtins, 'input', lambda *args: '11-2'):
            assert old_HW.delete_doc() == ('11-2', True)

    def test_delete_doc_false(self):
        with mock.patch.object(builtins, 'input', lambda *args: '11-3'):
            assert old_HW.delete_doc() == None