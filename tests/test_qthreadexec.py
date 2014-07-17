import pytest
import quamash


@pytest.fixture
def executor(request):
	exe = quamash.QThreadExecutor(5)
	request.addfinalizer(exe.shutdown)
	return exe


@pytest.fixture
def shutdown_executor():
	exe = quamash.QThreadExecutor(5)
	exe.shutdown()
	return exe


def test_shutdown_after_shutdown(shutdown_executor):
	with pytest.raises(RuntimeError):
		shutdown_executor.shutdown()


def test_ctx_after_shutdown(shutdown_executor):
	with pytest.raises(RuntimeError):
		with shutdown_executor:
			pass


def test_submit_after_shutdown(shutdown_executor):
	with pytest.raises(RuntimeError):
		shutdown_executor.submit(None)
